import logging
from odoo import models, fields, api, Command
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


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
    _room_no_uniq = models.Constraint('UNIQUE(room_number)','Room number must be unique!')
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
    member_ids = fields.Many2many('hostel.room.member', "hostel_room_member_rel", "room_id", "member_id", string='Members', check_company=True)
    hostel_amenities_ids = fields.Many2many("hostel.amenities", "hostel_room_amenities_rel", "room_id", "amenity_id", string="Amenities", domain="[('active', '=', True)]", help="Select hostel room amenities")
    student_per_room = fields.Integer(string="Student Per Room", required=True, default=1, store=True, help="Students allocated per room")
    availability = fields.Integer(string="Availability", compute='_compute_check_availability', store=True, help="Room availability in hostel") # compute_sudo=True because store=True makes the value computed even if the user doesn't have access to the field
    room_rating = fields.Float('Rooms Average Rating', digits='Rating Value')
    remarks = fields.Text('Remarks')
    previous_room_id = fields.Many2one('hostel.room', string='Previous Room')
    allocation_date = fields.Date(string="Allocation Date")

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_groups('hostel.group_hostel_manager'):
            for vals in vals_list:
                if vals.get('remarks'):
                    raise UserError(_('You are not allowed to modify remarks'))
        return super().create(vals_list)

    def write(self, vals):
        if not self.env.user.has_groups('hostel.group_hostel_manager'):
            if vals.get('remarks'):
                raise UserError('You are not allowed to modify remarks')
        if self.env.context.get('loop_breaker'):
            return True
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
    @api.depends_context('company_id')
    def _compute_check_availability(self):
        company_id = self.env.context.get('company_id')
        for record in self:
            record.availability = record.student_per_room - len(record.student_ids.ids)

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

    def log_all_members(self):
        hostel_members_obj = self.env['hostel.room.member']
        members = hostel_members_obj.search([])
        print("Room Members: ", members)
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
    def action_member_create(self):
        self.ensure_one()
        self.write({'student_ids': [
            # (0, 0, {'name': 'Nguyễn Văn Chuộn', 'member_code': 'NVC001'}),
            # (0, 0, {'name': 'Chần Kim Xuyến', 'member_code': 'TKX002'}),
            Command.create({'name': 'Nguyễn Văn Chuộn', 'member_code': 'NVC001'}),
            Command.create({'name': 'Tran Kim Xuyến', 'member_code': 'TKX002'}),
        ]})
        _logger.info('(0) Members: %s', self.student_ids.mapped('name'))

    # (1, id, vals): sửa bản ghi đang được gắn
    # = Command.update
    def action_member_update(self):
        self.ensure_one()
        member = self.student_ids[:1]
        if not member:
            raise UserError(_('Room has no member to update'))
        self.write({'student_ids': [
            # (1, member.id, {'name': member.name + ' (updated)'}),
            Command.update(member.id, {'name': member.name + ' (updated)'}),
        ]})
        _logger.info('(1) Members: %s', self.student_ids.mapped('name'))

    # (2, id): gỡ khỏi phòng VÀ xoá hẳn bản ghi khỏi DB
    # = Command.delete
    def action_member_delete(self):
        self.ensure_one()
        member = self.student_ids[:1]
        if not member:
            raise UserError(_('Room has no member to delete'))
        self.write({'student_ids': [
            # (2, member.id),
            Command.delete(member.id),
        ]})
        _logger.info('(2) Member %s exists in DB: %s', member.id, bool(member.exists()))

    # (3, id): chỉ gỡ khỏi phòng, bản ghi vẫn còn trong DB
    # = Command.unlink
    def action_member_unlink(self):
        self.ensure_one()
        member = self.student_ids[:1]
        if not member:
            raise UserError(_('Room has no member to remove'))
        self.write({'student_ids': [
            # (3, member.id),
            Command.unlink(member.id),
        ]})
        _logger.info('(3) Member %s exists in DB: %s', member.id, bool(member.exists()))

    # (4, id): gắn thêm bản ghi có sẵn, giữ member cũ
    # = Command.link
    def action_member_link(self):
        self.ensure_one()
        member = self.env['hostel.student'].search([('id', 'not in', self.student_ids.ids)], limit=1)
        if not member:
            raise UserError(_('No free member to add'))
        self.write({'student_ids': [
            # (4, member.id),
            Command.link(member.id),
        ]})
        _logger.info('(4) Members: %s', self.student_ids.mapped('name'))

    # (5,): gỡ toàn bộ member, không xoá bản ghi
    # = Command.clear()
    def action_member_clear(self):
        self.ensure_one()
        self.write({'student_ids': [
            # (5,),
            Command.clear(),
        ]})
        _logger.info('(5) Members: %s', self.student_ids.mapped('name'))

    # (6, 0, ids): thay toàn bộ danh sách bằng ids
    # = Command.set(ids)
    def action_member_replace(self):
        self.ensure_one()
        students = self.env['hostel.student'].search([], limit=2)
        self.write({'student_ids': [
            # (6, 0, student_ids.ids),
            Command.set(students.ids),
        ]})
        _logger.info('(6) Members: %s', self.student_ids.mapped('name'))

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
        filtered_rooms = self.is_has_multiple_members(rooms)
        # filtered_rooms = rooms.filtered(lambda r: len(r.student_ids) > 1)
        _logger.info('Filtered rooms %s', filtered_rooms)
        return True

    @api.model
    def is_has_multiple_members(self, rooms):
        def predicate(room):
            if len(room.student_ids) > 1:
                return True
            else:
                return False
        return rooms.filtered(predicate)

    # Traversing recordset
    def mapped_rooms(self):
        all_rooms = self.search([])
        room_members = self.get_member_names(all_rooms)
        _logger.info('Rooms Members: %s', room_members)

    @api.model
    def get_member_names(self, rooms):
        return rooms.mapped('student_ids.name')

    # Sorting recordset
    # không có tham số, _order của model sẽ được áp dụng
    # dataset quá lớn (> 50,000 phòng) => nên dùng search(order='room_rating DESC') để DB làm vì cho dù Python sort 50k record OK, nhưng PostgreSQL với index trên'room_rating' sẽ nhanh hơn nhiều + tiết kiệm RAM
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

    # Từ Odoo 17, name_get và _name_search không còn được Odoo gọi tới, nên 2 hàm override này không có tác dụng. 
    # Thay vào đó nên dùng _compute_display_name và _search_display_name.

    # def name_get(self):
    #     result = []
    #     for room in self:
    #         student_name = room.student_ids.mapped('name')
    #         name = '%s (%s)' % (room.name, ','.join(student_name))
    #         result.append((room.id, name))
    #     return result

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = [] if args is None else args.copy()
    #     if not (name == '' and operator == 'ilike'):
    #         args += ['|', '|', '|',
    #                  ('name', operator, name),
    #                  ('room_number', operator, name),
    #                  ('student_ids.name', operator, name)
    #                  ]
    #     return super(HostelRoom, self)._name_search(name=name, args=args, operator=operator, limit=limit,name_get_uid=name_get_uid)

    def grouped_data(self):
        grouped_data = self._get_average_cost()
        _logger.info('Grouped data %s', grouped_data)

    @api.model
    def _get_average_cost(self):
        grouped_result = self.env['hostel.room'].read_group(
            domain=['cost_price', '!=', 0],
            #fields=['category_id', 'cost_price:avg'],
            fields=['category_id', 'average_price:avg(cost_price)'],
            groupby=['category_id'],
            orderby='cost_price desc')
        return grouped_result

    # ======= Group theo category_id ==========
    @api.model
    def _get_room_report_by_category(self):
        grouped_result = self.env['hostel.room'].read_group(
            domain=['state', '!=', 'draft'],         # Lọc các phòng không ở draft
            fields=[
                'hostel_id',                         # Group theo hostel
                'rent_amount:sum',                   # Tổng tiền thuê (tổng)
                'rent_amount:avg',                   # Trung bình thuê (TB
                'rent_amount:count',                 # Đếm phòng
                'floor:max',                         # Tầng cao nhất
            ],
            groupby=['hostel_id'],                   # Group theo hostel
            having='rent_amount_sum > 0',                  
            orderby='rent_amount_sum desc'
        )
        return grouped_result

    # ======= Group theo state ==========
    @api.model
    def _get_room_report_by_state(self):
        grouped_result = self.env['hostel.room'].read_group(
            domain=[],
            fields=['rent_amount:sum'],
            groupby=['state']
        )
        return grouped_result

    @api.model
    def _expand_state_groups(self, states, domain=None, order=None):
        """
        Trả về danh sách tất cả các state (draft, available, closed) để hiển thị đầy đủ các cột trên Kanban/group.
        """
        return [(key, _label) for key, _label in self._fields['state'].selection]


    def log_all_room_students(self):
        # This is an empty recordset of model hostel.student
        students_empty = self.env['hostel.student']
        all_students = students_empty.search([])
        print("ALL Students:", all_students)
        return True

    