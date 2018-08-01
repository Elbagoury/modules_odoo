# -*- coding: utf-8 -*-
{
    'name': "Localink mail template",

    'summary': """
        Module Auneor Conseil 
        """,

    'description': """
        Module Auneor Conseil
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'odoo_marketplace'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mail_templates/invoice_mail_template.xml',
        'views/mail_templates/sale_order_mail_template.xml',
        'views/mail_templates/purchase_order_mail_template.xml',
        'views/mail_templates/vendor_bill_mail_template.xml',
        'views/res_partner_view.xml',
    ],
}