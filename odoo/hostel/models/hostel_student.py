from datetime import timedelta
from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError, AccessError, MissingError

class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}
    _check_company_auto = True
    _order = 'admission_date desc, id desc'

    # Chỉ giữ khai báo name khi inheritance là extension hoặc prototype
    # Ở đây không giữ khai báo name vì res.partner đã có name (ngoại trừ khi res.partner là extension hoặc prototype)
    # name = fields.Char("Student Name")
    gender = fields.Selection([("male", "Male"),("female", "Female"), ("other", "Other")], string="Gender", help="Student gender")
    active = fields.Boolean("Active", default=True, help="Activate/Deactivate hostel record")
    room_id = fields.Many2one("hostel.room", "Room", check_company=True, help="Select hostel room", ondelete='restrict')
    hostel_id = fields.Many2one("hostel.hostel", string="Hostel Name", related="room_id.hostel_id", related_sudo=True, check_company=True)
    status = fields.Selection([("draft", "Draft"),("reservation", "Reservation"),("pending", "Pending"),("paid", "Paid"),("discharge", "Discharge"),("cancel", "Cancel")], string="Status", copy=False, default="draft", help="State of the student hostel")
    admission_date = fields.Date('Admission Date', help='Enter student admission date', default=fields.Datetime.today)
    discharge_date = fields.Date('Discharge Date', help='Enter student discharge date')
    duration = fields.Integer('Duration', help='Enter student duration of living in hostel', compute='_compute_check_duration', inverse='_inverse_duration')
    member_number = fields.Char()
    member_code = fields.Char()
    date_of_birth = fields.Date('Date of birth')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, ondelete='cascade', delegate=True)

    @api.depends('admission_date', 'discharge_date')
    def _compute_check_duration(self):
        for record in self:
            if record.admission_date and record.discharge_date:
                record.duration = (record.discharge_date - record.admission_date).days
            else:
                record.duration = 0
                
    def _inverse_duration(self):
        for record in self:
            if record.admission_date and record.discharge_date:
                duration = (record.discharge_date - record.admission_date).days
                if duration != record.duration:
                    record.discharge_date = record.admission_date + timedelta(days=record.duration).strftime('%Y-%m-%d')

    def assign_room(self):
        self.ensure_one()
        if self.status != 'paid':
            raise UserError(self.env._("We can't assign a room if it's not paid"))
        
        # Lấy category phòng từ XML ID chính xác trong module hostel
        category = self.env.ref("hostel.room_category_single", raise_if_not_found=False)
        room_as_super = self.env['hostel.room'].sudo()
        room = room_as_super.create({
            "name": f"Room Auto-{self.id}",
            "room_number":  f"A-{self.id}",
            "floor": 1,
            "category_id": category.id if category else False,
        })
        
        self.room_id = room.id
        # Trong Odoo Web Client, một button handler chỉ xử lý 2 trường hợp:
        # Không trả về gì (return True): Web client sẽ giữ nguyên màn hình và reload dữ liệu form view hiện tại.
        # Trả về một Action Dictionary (ví dụ {'type': 'ir.actions.act_window', ...}): Web client sẽ mở màn hình/popup theo chỉ định.
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hostel.room',
            'res_id': room.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.onchange('room_id')
    def _onchange_room_id(self):
        if self.room_id and self.status == 'draft':
            self.status = 'reservation'

    @api.onchange('status')
    def _onchange_status_discharge(self):
        if self.status == 'discharge':
            self.update({
                'discharge_date': fields.Date.today(),
                'room_id': False
            })

    def action_remove_room(self):
        if self.env.context.get('is_hostel_room'):
            self.room_id = False