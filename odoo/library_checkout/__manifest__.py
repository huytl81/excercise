# -*- coding: utf-8 -*-
{
    'name': "Library Book Checkout",
    'summary': "Members can borrow books from the library.",
    'description': """
        Manage library book checkouts, return stages, and batch messages.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Library',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['library_member', 'mail'],

    # always loaded
    'data': [
        'security/ir.access.csv',
        'wizard/checkout_massmessage_wizard_form.xml',
        'views/library_menu.xml',
        'views/checkout_view.xml',
        'views/checkout_kanban_view.xml',
        'data/library_checkout_stage.xml',
    ],
    'demo': [],
}
