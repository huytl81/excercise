import logging
from os.path import join as opj
from odoo import models, fields, api, Command
from odoo.exceptions import UserError, ValidationError, MissingError, AccessError
from odoo.tools.translate import _

EXPORTS_DIR = "/opt/exercise/odoo/hostel/exports"

_logger = logging.getLogger(__name__)
# https://www.odoo.com/documentation/master/developer/reference/cli.html#logging
# _logger.debug, info, warning, error, critical
# Terminal: ‑‑log‑handler=prefix:level
# $ python3.10 ./odoo-bin --log-handler=odoo.addons.my_hostel:DEBUG
# $ python3.10 ./odoo-bin --log-handler=:ERROR,werkzeug:CRITICAL,odoo.service.server:INFO
# --- GLOBAL LOG LEVEL (--log-level) ---
# Cú pháp: python3.10 ./odoo-bin --log-level=<level>
# Các giá trị có thể dùng:
# 1. info (Mặc định): Ghi log thông thường (khởi động, request http status...)
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=info
# 2. warn: Chỉ log cảnh báo (warning) và lỗi (error/critical), bỏ qua info
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=warn
# 3. error: Chỉ log lỗi (exceptions/traceback) và critical
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=error
# 4. critical: Mức cao nhất, chỉ log các lỗi hệ thống nghiêm trọng
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=critical
# 5. debug: Hiển thị chi tiết thông tin gỡ lỗi của các tiến trình nội bộ
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=debug
# 6. debug_rpc: Log chi tiết các cuộc gọi RPC (gồm params gửi từ web/client)
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=debug_rpc
# 7. debug_rpc_answer: Log cả RPC request và dữ liệu phản hồi từ server
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=debug_rpc_answer
# 8. debug_sql: Log mọi câu truy vấn SQL thực thi xuống PostgreSQL kèm thời gian chạy
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=debug_sql
# 9. test: Dùng khi chạy unit test, lọc log phù hợp với testing
#    $ python3.10 ./odoo-bin -c odoo.conf --log-level=test --test-enable
# --- SHORTCUTS CHO LOGGING ---
# 1. --log-request: Viết tắt của --log-handler=odoo.http.rpc.request:DEBUG
#    Debug các request JSON-RPC/HTTP gửi từ web client lên backend
#    $ python3.10 ./odoo-bin -c odoo.conf --log-request
# 2. --log-response: Viết tắt của --log-handler=odoo.http.rpc.response:DEBUG
#    Debug dữ liệu phản hồi (response payload) trả về cho client
#    $ python3.10 ./odoo-bin -c odoo.conf --log-response
# 3. --log-web: Viết tắt của --log-handler=odoo.http:DEBUG
#    Debug tầng routing HTTP và controller của Odoo
#    $ python3.10 ./odoo-bin -c odoo.conf --log-web
# 4. --log-sql: Viết tắt của --log-handler=odoo.sql_db:DEBUG
#    Debug riêng các câu lệnh SQL mà không ảnh hưởng log-level toàn cục
#    $ python3.10 ./odoo-bin -c odoo.conf --log-sql

class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Base Archive'

    active = fields.Boolean(default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active

class HostelRoom(models.Model):
    _name = "hostel.room"
    _description = "Hostel Room"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'base.archive']
    #_sql_constraints = [("room_no_unique", "unique(room_number)", "Room number must be unique!")]
    _room_no_unique = models.Constraint('UNIQUE(room_number)','Room number must be unique!')
    _check_company_auto = True
    
    name = fields.Char(string="Room Name", required=True)
    description = fields.Text(string="Description")
    floor = fields.Integer(string="Floor", aggregator='max')
    image = fields.Binary(string="Image")
    state = fields.Selection([('draft', 'Unavailable'), ('available', 'Available'), ('closed', 'Closed')],string='State', default='draft', group_expand='_expand_state_groups')
    # active = fields.Boolean(string="Active", default=True)
    hostel_id = fields.Many2one(comodel_name='hostel.hostel', string="Hostel Name", ondelete='restrict', check_company=True, tracking=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, index=True, required=True)
    hostel_room_line_ids = fields.One2many(comodel_name='hostel.room.line', inverse_name='room_id', string='Lines', readonly=False)
    room_number = fields.Char(string="Room Number", required=True)
    room_type = fields.Selection([('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], string="Room Type", default='single')
    #currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    #rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month")
    hostel_room_currency = fields.Many2one(comodel_name="res.currency", string="Currency")
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month", currency_field='hostel_room_currency', aggregator='avg', tracking=2)
    cost_price = fields.Float('Room Cost', help="Enter room cost per month", company_dependent=True)
    category_id = fields.Many2one(comodel_name='hostel.room.category', string="Hostel Room Category")
    student_ids = fields.One2many(comodel_name="hostel.student", inverse_name="room_id", string="Students")
    hostel_amenities_ids = fields.Many2many("hostel.amenities", "hostel_room_amenities_rel", "room_id", "amenity_id", string="Amenities", domain="[('active', '=', True)]", help="Select hostel room amenities")
    student_per_room = fields.Integer(string="Student Per Room", required=True, default=1, store=True, help="Students allocated per room")
    availability = fields.Integer(string="Availability", compute='_compute_check_availability', store=True, help="Room availability in hostel") # compute_sudo=True because store=True makes the value computed even if the user doesn't have access to the field
    room_rating = fields.Float('Rooms Average Rating', digits='Rating Value')
    remarks = fields.Text('Remarks')
    previous_room_id = fields.Many2one('hostel.room', string='Previous Room')
    allocation_date = fields.Date(string="Allocation Date")

    # Trong create(self, vals_list) thì là list of dicts.
    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_groups('hostel.group_hostel_manager'):
            for vals in vals_list:
                if vals.get('remarks'):
                    raise UserError(_('You are not allowed to modify remarks'))
        return super().create(vals_list)

    # Trong write(self, vals) thì chỉ là 1 dict duy nhất, chứa các dirty fields (thực sự thay đổi)
    def write(self, vals):
        if not self.env.user.has_groups('hostel.group_hostel_manager'):
            if vals.get('remarks'):
                raise UserError('You are not allowed to modify remarks')
        if self.env.context.get('loop_breaker'):
            return True
        # Odoo không sửa đổi context toàn cục của hệ thống, chỉ tạo ra một bản sao self mới (với env mới) mang cờ loop_breaker=True cho riêng nhánh thực thi bên dưới nó.
        self = self.with_context(loop_breaker = True)
        sup = super(HostelRoom, self).write(vals)
        # self.compute_things()  # can cause calls to writes
        return sup

    def copy(self, default=None):
        # Gọi super() để sinh bản ghi copy
        new_room = super().copy(default=default)
        # Can thiệp sửa bản ghi kết quả trước khi return
        new_room.rent_amount = 0.0
        return new_room

    @api.model
    def _update_room_rent_amount(self):
        all_rooms = self.search([])
        for room in all_rooms:
            room.rent_amount += 10

    @api.model
    def _update_room_cost_price(self, category_id, amount_to_increase):
        _logger.info('Method update_room_price called from XML')
        category_rooms = self.search([('category_id', '=', category_id)])
        for room in category_rooms:
            room.cost_price += amount_to_increase

    @api.constrains('rent_amount')
    def _check_rent_amount(self):
        for record in self:
            if record.rent_amount < 0:
                msg = _("Rent amount must be positive!")
                raise ValidationError(msg)

    @api.constrains('hostel_id')
    def _check_hostel_id_change(self):
        for record in self:
            if record._origin.id and record._origin.hostel_id and record.hostel_id and record._origin.hostel_id != record.hostel_id:
                raise ValidationError(_(
                    "The room '%s' already belongs to hostel '%s'. "
                    "You cannot assign it to hostel '%s' directly. "
                    "Please clear its current hostel first."
                ) % (record.name, record._origin.hostel_id.name, record.hostel_id.name))

    @api.depends('student_per_room', 'student_ids')
    @api.depends_context('company')
    def _compute_check_availability(self):
        current_company = self.env.company
        for record in self:
            active_students = record.student_ids.filtered(lambda s: not s.company_id or s.company_id == current_company)
            record.availability = record.student_per_room - len(active_students)
            # record.availability = record.student_per_room - len(record.student_ids.ids)

    @api.model
    def _is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'), ('available', 'closed'), ('closed', 'draft')]
        return (old_state, new_state) in allowed
        # if (old_state, new_state) in allowed:
        #   return True
        # else:
        #   return False

    def _change_state(self, new_state):
        for record in self:
            if record._is_allowed_transition(record.state, new_state):
                record.state = new_state
            else:
                # msg = _('Transition from %s to %s is not allowed') % (record.state, new_state)
                msg = _('Transition from %s to %s is not allowed', record.state, new_state)
                raise UserError(msg)

    def make_available(self):
        self._change_state('available')

    def make_closed(self):
        self._change_state('closed')

    def log_all_students(self):
        hostel_students_obj = self.env['hostel.student']
        students = hostel_students_obj.search([])
        _logger.info("Room Students: %s", students)
        return True

    def update_room_no(self):
        self.ensure_one()

        # Option 1: Directly assign the room number
        # self.room_number = "R001"

        # Option 2: Use update method
        # self.update({
        #     'room_number': "R001",
        #     'floor': 1
        # })

        # Option 3: Use write method
        self.write({
            'room_number': "R001",
            'floor': 3,
            'state': 'available'
        })

    # (0, 0, vals): tạo bản ghi mới rồi gắn vào phòng
    # = [Command.create({...}), Command.create({...})]
    def action_student_create(self):
        self.ensure_one()
        self.write({'student_ids': [
            # (0, 0, {'name': 'Nguyễn Văn Chuộn', 'member_code': 'NVC001'}),
            # (0, 0, {'name': 'Chần Kim Xuyến', 'member_code': 'TKX002'}),
            Command.create({'name': 'Nguyễn Văn Chuộn', 'member_code': 'NVC001'}),
            Command.create({'name': 'Tran Kim Xuyến', 'member_code': 'TKX002'}),
        ]})
        _logger.info('(0) Students: %s', self.student_ids.mapped('name'))

    # (1, id, vals): sửa bản ghi đang được gắn
    # = Command.update
    def action_student_update(self):
        self.ensure_one()
        student = self.student_ids[:1]
        if not student:
            raise UserError(_('Room has no student to update'))
        self.write({'student_ids': [
            # (1, student.id, {'name': student.name + ' (updated)'}),
            Command.update(student.id, {'name': student.name + ' (updated)'}),
        ]})
        _logger.info('(1) Students: %s', self.student_ids.mapped('name'))

    # (2, id): gỡ khỏi phòng VÀ xoá hẳn bản ghi khỏi DB
    # = Command.delete
    def action_student_delete(self):
        self.ensure_one()
        student = self.student_ids[:1]
        if not student:
            raise UserError(_('Room has no student to delete'))
        self.write({'student_ids': [
            # (2, student.id),
            Command.delete(student.id),
        ]})
        _logger.info('(2) Student %s exists in DB: %s', student.id, bool(student.exists()))

    # (3, id): chỉ gỡ khỏi phòng, bản ghi vẫn còn trong DB
    # = Command.unlink
    def action_student_unlink(self):
        self.ensure_one()
        student = self.student_ids[:1]
        if not student:
            raise UserError(_('Room has no student to remove'))
        self.write({'student_ids': [
            # (3, student.id),
            Command.unlink(student.id),
        ]})
        _logger.info('(3) Student %s exists in DB: %s', student.id, bool(student.exists()))

    # (4, id): gắn thêm bản ghi có sẵn, giữ student cũ
    # = Command.link
    def action_student_link(self):
        self.ensure_one()
        student = self.env['hostel.student'].search([('id', 'not in', self.student_ids.ids)], limit=1)
        if not student:
            raise UserError(_('No free student to add'))
        self.write({'student_ids': [
            # (4, student.id),
            Command.link(student.id),
        ]})
        _logger.info('(4) Students: %s', self.student_ids.mapped('name'))

    # (5,): gỡ toàn bộ student, không xoá bản ghi
    # = Command.clear()
    def action_student_clear(self):
        self.ensure_one()
        self.write({'student_ids': [
            # (5,),
            Command.clear(),
        ]})
        _logger.info('(5) Students: %s', self.student_ids.mapped('name'))

    # (6, 0, ids): thay toàn bộ danh sách bằng ids
    # = Command.set(ids)
    def action_student_replace(self):
        self.ensure_one()
        students = self.env['hostel.student'].search([], limit=2)
        self.write({'student_ids': [
            # (6, 0, students.ids),
            Command.set(students.ids),
        ]})
        _logger.info('(6) Students: %s', self.student_ids.mapped('name'))

    def find_room(self):
        domain = [
            '|',
            '&', ('name', 'ilike', 'A25'),
            ('room_number', 'ilike', '01'),
            '&', ('name', 'ilike', 'Mai'),
            ('room_number', 'ilike', '02')
        ]

        rooms = self.search(domain, offset=0, limit=1000, order='name')
        # Chỉ cần đếm số phòng:
        room_count = self.search_count(domain)

        _logger.info('There are %s rooms found: %s', room_count, rooms)
        return True

    # Filtering recordset
    def filter_rooms(self):
        rooms = self.search([])
        filtered_rooms = self.is_has_multiple_students(rooms)
        # filtered_rooms = rooms.filtered(lambda r: len(r.student_ids) > 1)
        _logger.info('Filtered rooms %s', filtered_rooms)
        return True

    @api.model
    def is_has_multiple_students(self, rooms):
        def predicate(room):
            if len(room.student_ids) > 1:
                return True
            else:
                return False
        return rooms.filtered(predicate)

    # Traversing recordset
    def mapped_rooms(self):
        all_rooms = self.search([])
        room_students = self.get_student_names(all_rooms)
        _logger.info('Rooms Students: %s', room_students)

    @api.model
    def get_student_names(self, rooms):
        return rooms.mapped('student_ids.name')

    # Sorting recordset
    # không có tham số, _order của model sẽ được áp dụng
    # dataset quá lớn (> 50,000 phòng) => nên dùng search(order='room_rating DESC') để PostgreSQL xử lý 
    # Python sort 50k record OK nhưng PostgreSQL với index trên'room_rating' sẽ nhanh hơn nhiều + tiết kiệm RAM
    # dataset nhỏ => dùng như code bên dưới vì có cache, nếu dùng search(order='room_rating DESC') => lãng phí 1 lần query vào DB
    def sort_room(self):
        all_rooms = self.search([])
        rooms_sorted = all_rooms.sorted(key='room_rating', reverse=True)
        # rooms_sorted = self.sort_rooms_by_rating(all_rooms)
        _logger.info('Rooms before sorting: %s', all_rooms)
        _logger.info('Rooms after sorting: %s', rooms_sorted)

    # @api.model
    # def sort_rooms_by_rating(self, rooms):
    #     return rooms.sorted(key='room_rating', reverse=True)

    def grouped_data(self):
        grouped_data = self._get_average_cost()
        _logger.info('Grouped data %s', grouped_data)

    @api.model
    def _get_average_cost(self):
        grouped_result = self.env['hostel.room'].read_group(
            domain=[('cost_price', '!=', 0)],
            groupby=['category_id'],
            aggregates=['cost_price:avg'],
            order='cost_price:avg desc')
        return grouped_result

    # formatted_read_group, kết quả trả về dạng list[dict] => [{'category_id': (1, 'Deluxe'), 'cost_price:avg': 1500000.0, '__count': 3}, ...]
    # => tiện duyệt row['category_id'], row['cost_price:avg']
    # @api.model
    # def _get_average_cost(self):
    #     grouped_result = self.env['hostel.room'].formatted_read_group(
    #         domain=[('cost_price', '!=', 0)],
    #         groupby=['category_id'],
    #         aggregates=['cost_price:avg'],
    #         order='cost_price:avg desc'
    #     )
    #     return grouped_result

    # ======= Group theo category_id ==========
    @api.model
    def _get_room_report_by_category(self):
        grouped_result = self.env['hostel.room'].read_group(
            domain=[('state', '!=', 'draft')],       # Lọc các phòng trạng thái khác draft
            aggregates=[
                'rent_amount:sum',                   # Tổng tiền thuê
                'rent_amount:avg',                   # Trung bình tiên thuê
                'rent_amount:count',                 # Đếm số phòng
                'floor:max',                         # Tầng cao nhất
            ],
            groupby=['hostel_id'],                   # Group theo hostel
            having=[('rent_amount:sum', '>', 0)],                
            order='rent_amount:sum desc'
        )
        return grouped_result

    # ======= Group theo state ==========
    @api.model
    def _get_room_report_by_state(self):
        grouped_result = self.env['hostel.room'].read_group(
            domain=[],
            aggregates=['rent_amount:sum'],
            groupby=['state']
        )
        return grouped_result

    @api.model
    def _expand_state_groups(self, states, domain=None, order=None):
        """
        Trả về danh sách tất cả các state (draft, available, closed) để hiển thị đầy đủ các cột trên Kanban/group.
        """
        # return [(key, _label) for key, _label in self._fields['state'].selection]
        return [key for key,_lable in self._fields['state'].selection]

    def log_all_room_students(self):
        # This is an empty recordset of model hostel.student
        students_empty = self.env['hostel.student']
        all_students = students_empty.search([])
        print("ALL Students:", all_students)
        return True
    # pdb debugger
    # https://docs.python.org/3/library/pdb.html
    @api.model
    def export_available_rooms(self):
        import pdb; pdb.set_trace()
        # Chay truc tiep trong shell
        # >>> import pdb
        # >>> room = env['hostel.room']
        # >>> pdb.runcall(room.export_available_rooms)
        _logger.info("Starting export of available hostel rooms")
        rooms_available_to_export = self.search([('state', '=', 'available')])
        _logger.debug("Found %d available rooms", len(rooms_available_to_export))
        file_path = opj(EXPORTS_DIR, "available_rooms.txt")
        try:
            with open(file_path, 'w') as f:
                for room in rooms_available_to_export:
                    _logger.debug("Writing Room %s | Number %s | Rating %s", room.name, room.room_number, room.room_rating)
                    f.write(f"{room.name}\t{room.room_number}\t{room.room_rating or 0.0}\n")
            _logger.info("Room export completed successfully: %s", file_path)
        except IOError:
            _logger.exception("Error while writing room data to file: %s", file_path)
            raise UserError("Unable to export room data!")

    def action_remove_room_students(self):
        self.student_ids.with_context(is_hostel_room=True).action_remove_room()