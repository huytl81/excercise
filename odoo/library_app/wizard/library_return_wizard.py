# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class LibraryReturnWizard(models.TransientModel):
    _name = 'library.return.wizard'
    _description = 'Return Books Wizard'

    borrower_id = fields.Many2one('res.partner', string='Borrower', required=True)
    book_ids = fields.Many2many(
        'library.book',
        string='Books',
        compute='_compute_book_ids',
        readonly=False,
        store=True,
    )

    @api.depends('borrower_id')
    def _compute_book_ids(self):
        for wizard in self:
            if wizard.borrower_id:
                loans = self.env['library.book.rent'].search([
                    ('stage_id.book_state', '=', 'borrowed'),
                    ('borrower_id', '=', wizard.borrower_id.id),
                ])
                wizard.book_ids = loans.mapped('book_id')
            else:
                wizard.book_ids = False

    @api.onchange('borrower_id')
    def onchange_member(self):
        if not self.borrower_id:
            return {'domain': {'book_ids': [('id', '=', False)]}}

        rent_model = self.env['library.book.rent']
        books_on_rent = rent_model.search([
            ('stage_id.book_state', '=', 'borrowed'),
            ('borrower_id', '=', self.borrower_id.id),
        ])
        borrowed_books = books_on_rent.mapped('book_id')
        self.book_ids = borrowed_books

        result = {
            'domain': {
                'book_ids': [('id', 'in', borrowed_books.ids)]
            }
        }

        late_books = books_on_rent.filtered(
            lambda r: r.expected_return_date and r.expected_return_date < fields.Date.today()
        )
        if late_books:
            message = _('Warn the member that the following books are late:\n')
            titles = late_books.mapped('book_id.name')
            result['warning'] = {
                'title': _('Late books'),
                'message': message + '\n'.join(titles),
            }
        return result

    def books_returns(self):
        self.ensure_one()
        rent_model = self.env['library.book.rent']
        loans = rent_model.search([
            ('stage_id.book_state', '=', 'borrowed'),
            ('book_id', 'in', self.book_ids.ids),
            ('borrower_id', '=', self.borrower_id.id),
        ])
        for loan in loans:
            loan.book_return()
        return {'type': 'ir.actions.act_window_close'}
