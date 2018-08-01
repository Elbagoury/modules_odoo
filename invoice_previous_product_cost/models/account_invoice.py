# -*- encoding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import Warning


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    invoice_partner_id = fields.Many2one(related='invoice_id.partner_id', store=True, string='Customer')
    invoice_data = fields.Date(comodel_name='account.invoice', string='Invoice Date',
                               related='invoice_id.date_invoice', store=True)
    invoice_state = fields.Selection(comodel_name='account.invoice', string='Invoice State',
                                     related='invoice_id.state', store=True)


class ProductProduct(models.Model):
    _inherit = "product.product"

    invoice_partner_id = fields.Many2one('res.partner', string="Partner")

    @api.multi
    def action_invoice_product_prices(self):
        rel_view_id = self.env.ref(
            'invoice_previous_product_cost.last_invoice_product_invoice_prices_view')
        invoice_lines = self.env['account.invoice.line'].search([('product_id', '=', self.id),
                                                                 ('invoice_partner_id', '=', self.invoice_partner_id.id),
                                                                 ('invoice_state', '!=', 'paid')],
                                                                order='create_date DESC')
        if not invoice_lines:
            raise Warning("No sale history found.!")
        else:
            return {
                'view_type': 'tree',
                'view_mode': 'tree',
                'res_model': 'account.invoice.line',
                'views': [(rel_view_id.id, 'tree')],
                'view_id': False,
                'type': 'ir.actions.act_window',
                'target': 'new',
                'domain': "[('id','in',[" + ','.join(map(str, invoice_lines.ids)) + "])]",
            }


class ProductTemplate(models.Model):
    _inherit = "product.template"

    last_invoice_price = fields.Float(string="Last invoice price", compute='_get_last_product')

    def _get_last_product(self):
        for record in self:
            res = record.env['account.invoice.line'].search([('product_id', '=', record.id),
                                     ('invoice_state', '!=', 'draft')],
                                    order='create_date DESC', limit=1)
            record.last_invoice_price = res.price_unit

    @api.multi
    def action_invoice_product_prices(self):
        rel_view_id = self.env.ref(
            'invoice_previous_product_cost.last_invoice_product_invoice_prices_view')
        invoice_lines = self.env['account.invoice.line'].search([('product_id', '=', self.id),
                                                                 ('invoice_state', '!=', 'draft')],
                                                                order='create_date DESC')
        if not invoice_lines:
            raise Warning("No sale history found.!")
        else:
            return {
                'view_type': 'tree',
                'view_mode': 'tree',
                'res_model': 'account.invoice.line',
                'views': [(rel_view_id.id, 'tree')],
                'view_id': False,
                'type': 'ir.actions.act_window',
                'target': 'new',
                'domain': "[('id','in',[" + ','.join(map(str, invoice_lines.ids)) + "])]",
            }
