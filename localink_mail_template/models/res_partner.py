# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner.title'

    genders = [
        ('masculin', 'Masculin'),
        ('feminin', 'Féminin'),
    ]

    gender = fields.Selection(genders, string='Genre')
