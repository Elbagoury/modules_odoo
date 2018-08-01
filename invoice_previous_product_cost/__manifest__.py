# -*- coding: utf-8 -*-
{
    'name': "Invoice previous product cost",

    'summary': """
        Provide Product's Previous Invoice Price History.""",

    'description': """
        This module provide product's previous prices in product and sale order/quotation form of selected customer.
        Draft invoices not displayed
    """,

    'author': "Auneor-Conseil",
    'website': "http://www.auneor-conseil.fr",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['account',
                'sale'],

    'data': [
        'views/account_invoice_view.xml',
        'views/product_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}
