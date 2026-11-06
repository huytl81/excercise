# -*- coding: utf-8 -*-
{
    'name': "Hostel Management",
    'summary': "Manage Hostel easily",
    'description': """
           Efficiently manage the entire residential 
           facility in the school.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Uncategorized',
    'version': '20.0.1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'depends': ['base', 'mail'],
    # always loaded
    'data': [
        'data/data.xml',
        'data/hostel.room.csv',
        'security/hostel_security.xml',
        'security/ir.access.csv',
        'views/hostel_category.xml',
        'views/hostel.xml',
        'views/hostel_room.xml',
        'views/hostel_student.xml',
        'views/hostel_room_category.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'web/static/src/xml/**/*',
        ],
    },
    'post_init_hook': '_update_company_email',
}

