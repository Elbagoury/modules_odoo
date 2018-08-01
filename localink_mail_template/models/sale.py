from odoo import api, fields, models
from datetime import timedelta, datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_estimated_date = fields.Datetime(compute='_estimated_date')

    @api.depends('confirmation_date')
    def _estimated_date(self):
        if self.confirmation_date:
            self.delivery_estimated_date = datetime.strptime(self.confirmation_date,"%Y-%m-%d %H:%M:%S") + timedelta(days=1)
