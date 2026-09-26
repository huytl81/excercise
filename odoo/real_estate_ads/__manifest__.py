# -*- coding: utf-8 -*-
{
    'name': 'Real Estate Ads',
    'summary': 'Manage real estate properties and ads',
    'description': """
        Manage real estate property ads, types, tags, and offers.
    """,
    'author': 'Huy Ta',
    'website': 'https://www.odoovn.info',
    'category': 'Real Estate',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'website', 'web'],

    # always loaded
    'data': [
        # Security
        'security/access_groups.xml',
        'security/ir.access.csv',
        # Views
        'views/property_view.xml',
        'views/property_offer_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_web_template.xml',
        # Action
        'views/property_actions.xml',
        # Data files
        'data/property_type.xml',
        'data/estate.property.tag.csv',
        'data/mail_template.xml',
        # Report
        'report/report_template.xml',
        'report/property_report.xml',
    ],
    # Demo
    'demo': [
        'demo/property.xml',
    ],
    # Assets
    'assets': {
        'web.assets_backend': [
            'real_estate_ads/static/src/js/my_custom_tag.js',
            'real_estate_ads/static/src/xml/my_custom_tag_template.xml',
        ],
    },
}
