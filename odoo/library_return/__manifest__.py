# -*- coding: utf-8 -*-
{
    'name': "My Library Returns Dates",
    'summary': "Manage return dates for books",
    'description': """
        Manage book return dates and due calculations.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Library',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['library_app'],

    # always loaded
    'data': [
        'views/library_book.xml',
    ],
    'demo': [],
}
