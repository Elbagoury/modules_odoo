# -*- encoding: utf-8 -*-

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def set_partner(self):
        for each in self:
            print each.order_id.partner_id.id
            if each.product_id:
                each.product_id.write({'invoice_partner_id': each.order_id.partner_id.id})
