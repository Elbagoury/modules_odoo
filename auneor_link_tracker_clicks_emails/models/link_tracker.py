# -*- coding: utf-8 -*-

from odoo import models, api


class AuneorConseilLinkTrackerClicksEmails(models.Model):
    _inherit = "link.tracker"

    @api.multi
    @api.depends('link_click_ids')
    def contacts_list_view(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mail.mail.statistics',
            'view_mode': 'tree',
            'view_id': self.env.ref('mass_mailing.view_mail_mail_statistics_tree').id,
            'target': 'new',
            'domain': [('id', 'in', [x.mail_stat_id.id for x in self.link_click_ids])]
        }
