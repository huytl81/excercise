from odoo import models, fields, api, _


class HostelRoomExtend(models.Model):
    _name = "hostel.room.copy"
    _description = "Hostel Room Information Extend"
    _inherit = "hostel.room"

    hostel_amenities_ids = fields.Many2many("hostel.amenities", "hostel_room_extend_amenities_rel", "room_id","amenity_id", string="Amenities", domain="[('active', '=', True)]", help="Select hostel room amenities")