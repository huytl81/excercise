# -*- coding: utf-8 -*-
{
    'name': "Todolist management with OWL",

    'summary': "Todolist management with OWL",

    'description': """
        ... by meobeongaongo
    """,

    'author': "meobeongaongo",
    'website': "https://www.odoovn.info",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customize Application',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'data': [
        'security/todo_task_security.xml',
        'security/todo_task_access.xml',
        'security/ir.model.access.csv',
        'views/club_view.xml',
        'views/player_view.xml',
        'views/dog_view.xml',
        'views/cat_view.xml',
        'wizards/dog_wizard_view.xml',
        'views/todo_task.xml',
    ],
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
    }

}
