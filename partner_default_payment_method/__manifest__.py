# -*- coding: utf-8 -*-
{
    'name': "Default partner payment method",

    'summary': """
        This modules allow to set default payment method to partner""",

    'description':
        """
This modules allow to set default payment method to partner.
This payment method then defaults in sale order and invoice.

    """,

    'author': "Adrien Combourieu - Aunéor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        # 'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
