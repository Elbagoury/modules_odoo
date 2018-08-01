# -*- coding: utf-8 -*-

from openerp import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    formation_reports = fields.Many2one('formation.formation', string="Rapports formation")
