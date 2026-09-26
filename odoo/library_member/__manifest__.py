# -*- coding: utf-8 -*-
{
    'name': "Library Members",
    'summary': "Manage members borrowing books.",
    'description': """
        Manage library members and their book borrowing history.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Library',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['library_app', 'mail'],

    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.access.csv',
        'views/library_book.xml',
        'views/member_view.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
