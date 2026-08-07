from odoo import models, fields, api

class HostelStudentExtended(models.Model):
    _description = 'Hostel Student Extended'
    _inherit = 'hostel.student'

    guardian_name = fields.Char(string='Guardian Name')
    student_code = fields.Char(string='Student Code')