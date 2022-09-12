# -*- coding: utf-8 -*-
{
    'name': "hello_world",

    'summary': """
        vakon nako
        kraj
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "bring.out",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'assets': {
        'web.assets_qweb': [
            'hello_world/static/src/xml/*.xml',
        ],
        'web.assets_backend': [ 
             'hello_world/static/src/js/main.js', 
             'hello_world/static/src/css/main.css',  
         ],
    },
    'installable': True,
    'application': True,
}
