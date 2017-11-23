# -*- coding: utf-8 -*-
{
    'name': "OdooTesting",

    'summary': """
        demo module for testing new functionalities """,

    'description': """
   	This module purpose is to test scheduling and notifications 
	""",

    'author': "Muuyal - Israel Soto",
    'website': "http://www.muuyal.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/pagos.xml',
        'views/odootest.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
