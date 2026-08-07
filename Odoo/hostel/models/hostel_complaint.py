from odoo import models, fields, api

class HostelComplaimt(models.Model):
    _name = 'hostel.complaint'
    _description = 'Hostel Complaint'
    _check_company_auto = True

    name = fields.Char(string='Complaint Title', required=True)
    description = fields.Text(string='Depict')
    date = fields.Date(string='Date', default=fields.Date.today())
    target_object_id = fields.Reference(selection=[('hostel.room', 'Room'), ('hostel.student', 'Student')],string='Complaint About')
