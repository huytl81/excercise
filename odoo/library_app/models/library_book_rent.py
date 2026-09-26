# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    _description = "Book Rent"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char('Book Rent')

    @api.model
    def _default_rent_stage(self):
        Stage = self.env['library.rent.stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stages(self, stages, domain, order=None):
        return stages.search([], order=order)

    book_id = fields.Many2one('library.book', 'Book', required=True)
    borrower_id = fields.Many2one('res.partner', 'Borrower', required=True)
    stage_id = fields.Many2one('library.rent.stage', default=_default_rent_stage, group_expand=_group_expand_stages)
    state = fields.Selection(
        [('ongoing', 'Ongoing'), ('returned', 'Returned'), ('lost', 'Lost')],
        string='State',
        compute='_compute_state',
        store=True,
        readonly=False,
    )
    rent_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    expected_return_date = fields.Date()

    color = fields.Integer()
    popularity = fields.Selection([('no', 'No Demand'), ('low', 'Low Demand'), ('medium', 'Average Demand'), ('high', 'High Demand'), ('critical', 'Highest Demand')])
    tag_ids = fields.Many2many('library.rent.tag')

    @api.depends('stage_id', 'stage_id.book_state', 'return_date')
    def _compute_state(self):
        for rec in self:
            if rec.stage_id.book_state == 'borrowed':
                rec.state = 'ongoing'
            elif rec.stage_id.book_state == 'lost':
                rec.state = 'lost'
            elif rec.return_date or rec.stage_id.book_state == 'available':
                rec.state = 'returned'
            else:
                rec.state = 'ongoing'

    @api.model_create_multi
    def create(self, vals_list):
        rents = super().create(vals_list)
        for rent in rents:
            if rent.stage_id.book_state:
                rent.book_id.state = rent.stage_id.book_state
        return rents

    def write(self, vals):
        res = super().write(vals)
        for rent in self:
            if rent.stage_id.book_state:
                rent.book_id.state = rent.stage_id.book_state
        return res

    def book_lost(self):
        lost_stage = self.env.ref('library_app.stage_lost', raise_if_not_found=False)
        vals = {'return_date': fields.Date.today()}
        if lost_stage:
            vals['stage_id'] = lost_stage.id
        for rent in self:
            rent.write(vals)
            new_context = dict(self.env.context, avoid_deactivate=True)
            rent.book_id.with_context(new_context).sudo().make_lost()

    def book_return(self):
        returned_stage = self.env.ref('library_app.stage_returned', raise_if_not_found=False)
        vals = {'return_date': fields.Date.today()}
        if returned_stage:
            vals['stage_id'] = returned_stage.id
        for rent in self:
            rent.book_id.make_available()
            rent.write(vals)


class LibraryRentStage(models.Model):
    _name = 'library.rent.stage'
    _description = 'Library Rent Stage'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()
    book_state = fields.Selection([('available', 'Available'), ('borrowed', 'Borrowed'), ('lost', 'Lost')], 'State', default="available")
    active = fields.Boolean("Active?", default=True)


class LibraryRentTags(models.Model):
    _name = 'library.rent.tag'
    _description = 'Library Rent Tag'

    name = fields.Char()
    color = fields.Integer()