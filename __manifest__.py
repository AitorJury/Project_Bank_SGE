# -*- coding: utf-8 -*-
{
    'name': "My Bank",
    'application': True,
    'summary': """
        Module for managing accounts and clients.""",

    'description': """
        Module for managing a user's bank accounts, the transactions of 
	each account, and, in the case of the administrator, the clients 
	created who can manage their accounts
    """,

    'author': "3th group from DAM",
    'website': "https://site.educa.madrid.org/ies.sanjuandelacruz.pozuelodealarcon/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bank.xml',
        'views/account.xml',
        'views/customer.xml',
        'views/movement.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
