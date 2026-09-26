from odoo import fields, models, api, _
from odoo.fields import Domain
# from odoo.models import to_record_ids


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = "Information about hostel"
    _rec_name = 'hostel_code'
    _rec_names_search = ['name', 'hostel_code', 'email', 'mobile']
    _check_company_auto = True

    def _check_company_domain(self, companies) -> Domain:
        # Gọi function gốc (trả về list/tuple biểu thức domain dạng => ['|', ('company_id', '=', False), ('company_id', 'parent_of', ...)])
        # sau đó wrap vào Domain object
        raw_domain = models.check_company_domain_parent_of(self, companies)
        return Domain(raw_domain) # Tương đương viết: Domain('company_id', '=', False) | Domain('company_id', 'parent_of', '...')

    #  ĐÚNG về runtime (Odoo vẫn chạy được) nhưng SAI về typing → đỏ
    # _check_company_domain = models.check_company_domain_parent_of

    _translate = True # or False
    _allow_sudo_commands = False # or True "Allow One2many and Many2many commands targeting this model in an environment using sudo() or with_user()"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Hostel Name", required=True)
    hostel_code = fields.Char(string="Hostel Code", required=True)
    category_id = fields.Many2one(comodel_name='hostel.category', string="Hostel Category")
    street = fields.Char('Street', required=True)
    street2 = fields.Char('Street2')
    state_id = fields.Many2one("res.country.state", string='State', check_company=False)
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City', aggregator='array_agg')
    country_id = fields.Many2one('res.country', string='Country', check_company=False)
    phone = fields.Char('Phone', required=True)
    mobile = fields.Char('Mobile', required=True)
    email = fields.Char('Email')
    hostel_floors = fields.Integer(string="Total Floors")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, index=True, required=True)  # Auto‑check company consistency
    image = fields.Binary('Hostel Image')
    active = fields.Boolean("Active", default=True, help="Activate/Deactivate hostel record", aggregator='bool_and')
    type = fields.Selection([("male", "Boys"), ("female","Girls"),("common", "Common")], "Type", help="Type of Hostel",required=True, default="male")
    other_info = fields.Text("Other Information", translate=True, help="Enter more information")
    description = fields.Html('Description', translate=True)
    #hostel_rating = fields.Float('Hostel Average Rating',digits=(14, 4)) # Method 1: Optional precision (total,decimals)
    hostel_rating = fields.Float('Hostel Average Rating', digits = 'Rating Value')  # Method 2
    hostel_room_line_ids = fields.One2many('hostel.room.line', inverse_name='hostel_id', string="Rooms")
    list_models = fields.Reference(selection='_list_models', string='List All Models')
    partner_user_models = fields.Selection(selection=[('res.partner', 'Partners'), ('res.users', 'Users')], string="Partners / Users", default='res.partner')
    corresponding_records = fields.Many2oneReference(model_field='partner_user_models', string='Related Records')
    room_count = fields.Integer(string='Hostel room count', compute='_compute_room_count', inverse='_inverse_room_count', search='_search_room_count', store=True, readonly=False)

    @api.depends('hostel_code')
    def _compute_display_name(self):
        for record in self:
            record_name = record.name or ''
            if record.hostel_code:
                record.display_name = f'{record_name} ({record.hostel_code})'
            else:
                record.display_name = f'{record_name}'

    @api.model
    def _list_models(self):
        # models = self.env['ir.model'].search([('field_id.name', '=', 'message_ids')])
        list_models = self.env['ir.model'].search([])
        return [(m.model, m.name) for m in list_models]

    @api.model
    def _get_hostel_report_by_country(self):
        grouped_results = self.env['hostel.hostel'].read_group(
            domain=[],
            fields=['city','active','avg_rating:avg(hostel_rating)'],
            groupby=['country_id']
        )
        return grouped_results

    @api.depends('hostel_room_line_ids')
    def _compute_room_count(self):
        for record in self:
            record.room_count = len(record.hostel_room_line_ids)
    
    def _inverse_room_count(self):
        # """Khi user sửa field room_count trên form → method này chạy:"""
        for record in self:
            current_count = len(record.hostel_room_line_ids)
            target = record.room_count or 0
            if current_count < target:
                # Tạo thêm phòng cho đủ số lượng
                Room = self.env['hostel.room']
                RoomLine = self.env['hostel.room.line']
                for i in range(target - current_count):
                    new_room_no = f"{record.hostel_code or 'R'}-{current_count + i + 1}"
                    room = Room.create({
                        'name': _('Room Auto-create #%d') % (current_count + i + 1),
                        'room_number': new_room_no,
                        'student_per_room': 1,
                        'company_id': record.company_id.id,
                    })
                    RoomLine.create({
                        'hostel_id': record.id,
                        'room_id': room.id,
                    })
            elif current_count > target:
                # Xóa bớt phòng cho đúng số
                excess = record.hostel_room_line_ids[target:]
                excess.unlink()
    
    def _search_room_count(self, operator='ilike', value=''):
        # operator: '=', '>', '<', '>=', ...
        # value: giá trị người dùng nhập vào form
        if operator == '>' and value == 10:
            # Cách 1: SQL query thô (giữ lại để tham khảo):
            # self.env.cr.execute("""
            #     SELECT hostel_id FROM hostel_room
            #     GROUP BY hostel_id HAVING COUNT(*) > %s
            # """, (value,))
            # ids = [row[0] for row in self.env.cr.fetchall()]
            # return [('id', 'in', ids)]

            # Cách 2: dùng ORM/Python, không chạy SQL thô.
            hostels = self.search([])
            matched_hostels = hostels.filtered(
                lambda h: len(h.hostel_room_line_ids) > value
            )
            return [('id', 'in', matched_hostels.ids)]
        return []
