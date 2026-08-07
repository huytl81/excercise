# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HostelRoomLine(models.Model):
    _name = 'hostel.room.line'
    _description = 'Hostel Room Line'
    _check_company_auto = True
    
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, required=True, index=True)  # Auto‑check company consistency
    hostel_id = fields.Many2one('hostel.hostel', string="Hostel", ondelete='cascade', required=True)
    room_id = fields.Many2one('hostel.room', string="Room", check_company=True, domain="[('hostel_id', '=', False)]", required=True)
    
    # Related fields to show information of the selected room
    room_number = fields.Char(related='room_id.room_number', string="Room Number", readonly=True)
    room_type = fields.Selection(related='room_id.room_type', string="Room Type", readonly=True)
    rent_amount = fields.Monetary(related='room_id.rent_amount', string="Rent Amount", readonly=True)
    currency_id = fields.Many2one(related='room_id.hostel_room_currency', string="Currency", readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        lines = super().create(vals_list)
        for line in lines:
            if line.room_id:
                line.room_id.hostel_id = line.hostel_id
        return lines

    def write(self, vals):
        if 'room_id' in vals:
            # Clear old rooms before write
            for line in self:
                if line.room_id:
                    line.room_id.hostel_id = False
        res = super().write(vals)
        if 'room_id' in vals:
            # Set new rooms after write
            for line in self:
                if line.room_id:
                    line.room_id.hostel_id = line.hostel_id
        return res

    def unlink(self):
        for line in self:
            if line.room_id:
                line.room_id.hostel_id = False
        return super().unlink()
