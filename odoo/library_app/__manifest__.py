# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'summary': "Manage library catalog and book lending.",
    'description': """
        Manage library catalog, book lending, and member rentals.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Library',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'base_setup', 'mail', 'contacts', 'website', 'utm'],

    # always loaded
    'data': [
        'data/data.xml',
        'data/library_stage.xml',
        'security/library_security.xml',
        'security/ir.access.csv',
        'views/res_config_settings_views.xml',
        'views/library_menu.xml',
        'views/library_book.xml',
        'views/library_book_category.xml',
        'views/book_list_template.xml',
        'views/res_partner_extend_view.xml',
        'views/library_book_rent.xml',
        'views/library_book_rent_wizard.xml',
        'views/library_book_return_wizard.xml',
        'views/templates.xml',
        'reports/book_rent_templates.xml',
        'reports/book_rent_report.xml',
        'reports/library_book_catalog_template.xml',
        'reports/library_book_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/res.partner.csv',
        'data/library.book.csv',
        'data/book_demo.xml',
    ],
}
