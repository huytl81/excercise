# -*- coding: utf-8 -*-
{
    'name': "Real Estate Ads - Sales Person",
    'summary': "Manage real estate properties and ads by sales person",
    'description': """
        Show real estate properties linked to sales person.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Real Estate',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['real_estate_ads', 'base', 'mail'],

    # always loaded
    'data': [
        'views/res_users.xml',
    ],
    'demo': [],
}
