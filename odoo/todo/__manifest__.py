# -*- coding: utf-8 -*-
{
    'name': "Todolist management with OWL",
    'summary': "Todolist management with OWL",
    'description': """
        Todolist management with OWL component framework.
    """,
    'author': "Huy Ta",
    'website': "https://www.odoovn.info",
    'category': 'Productivity',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/todo_task_security.xml',
        'security/ir.access.csv',
        'views/club_view.xml',
        'views/player_view.xml',
        'views/dog_view.xml',
        'views/cat_view.xml',
        'wizards/dog_wizard_view.xml',
        'views/todo_task.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            # Services
            'todo/static/src/services/todo_task_service.js',
            'todo/static/src/services/user_service.js',

            # Form Component
            'todo/static/src/xml/todo_task_popup_modal.xml',
            'todo/static/src/js/todo_task_popup_modal.js',

            # Main Component - Must be last
            'todo/static/src/xml/todo_task_action.xml',
            'todo/static/src/js/todo_task_action.js',
        ]
    },
}
