from datetime import timedelta
from odoo import models, api, fields
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _

class HostelRoom(models.Model):
    _inherit = 'hostel.room'

    category_id = fields.Many2one("hostel.room.category", string="Category")
    date_terminate = fields.Date('Date of Termination', help='Enter date of termination')

    @api.depends('room_number')
    def _compute_display_name(self):
        for record in self:
            record.display_name = (
                f"{record.name} - {record.room_number}"
                if record.room_number and record.name else record.name or ""
                )
                
    def make_closed(self):
        # 1. TRƯỚC: Tính ngày kết thúc
        day_to_allocate = self.category_id.max_allow_days or 10
        self.date_terminate = fields.Date.today() + timedelta(days=day_to_allocate)

        # 2. GỐC: Đổi trạng thái sang 'closed'
        res = super(HostelRoom, self).make_closed()

        # 3. SAU: Ghi log vào chatter
        self.message_post(body=f"Phòng đã đóng. Ngày hết hạn lưu trú: {self.date_terminate}")

        return res

    def make_available(self):
        self.date_terminate = False
        return super(HostelRoom,self).make_available()

    # Ở module kế thừa: chỉ cần can thiệp đúng điểm hook này
    @api.model
    def _is_allowed_transition(self, old_state, new_state):
        if old_state == 'closed' and new_state == 'available':
            return True
        return super()._is_allowed_transition(old_state, new_state)
