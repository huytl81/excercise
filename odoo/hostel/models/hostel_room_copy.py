from odoo import models, fields, api, _


class HostelRoomExtend(models.Model):
    _name = "hostel.room.copy"
    _description = "Hostel Room Information Extend"
    _inherit = "hostel.room"

    member_ids = fields.Many2many(
        'hostel.room.member', 'hostel_room_copy_member_rel', 'room_id', 'member_id',
        string='Members', check_company=True)
    hostel_amenities_ids = fields.Many2many(
        "hostel.amenities", "hostel_room_copy_amenities_rel", "room_id", "amenity_id",
        string="Amenities", domain="[('active', '=', True)]",
        help="Select hostel room amenities")
    # hostel_amenities_ids = fields.Many2many("hostel.amenities", "hostel_room_extend_amenities_rel", "room_id","amenity_id", string="Amenities", domain="[('active', '=', True)]", help="Select hostel room amenities")