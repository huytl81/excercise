# -*- coding: utf-8 -*-
{
    'name': "Library Portal",
    'summary': "Portal for library members",
    'description': """
        Portal features for library members to browse books and view checkouts.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Library',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['library_checkout', 'portal'],

    # always loaded
    'data': [
        'security/ir.access.csv',
        'views/portal_templates.xml',
        'views/catalog_template.xml',
        'views/snippets.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'library_portal/static/src/css/library_portal.css',
        ],
    },
}
