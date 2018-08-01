# -*- coding: utf-8 -*-
{
    'name': "Auneor Conseil link tracker clicks emails",

    'summary': """
        Display contacts who clicked on the links given in a email (link example: Facebook, Website...)""",

    'description': """
        This module adds a button on link tracker view, that open a new window displaying the contacts who clicked on 
        the links given in the email.
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['link_tracker', 'mail', 'mass_mailing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/link_tracker_views.xml',
    ],
}