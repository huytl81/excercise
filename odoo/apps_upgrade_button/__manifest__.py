# -*- coding: utf-8 -*-
{
    'name': "Quick actions in Apps",
    'summary': "Quick actions in Apps",
    'description': """
        Adds quick upgrade and action buttons in Apps view.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Extra Tools',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'views/upgrade_button_views.xml',
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
}
