# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        invoice.sale_order_id = order
        invoice.payment_method_id = order.payment_method_id
        return invoice


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    payment_method_id = fields.Many2one(comodel_name="account.journal",
                                        string="Payment Method",
                                        required=False,
                                        domain=[('type', 'in', ['cash', 'bank'])]
                                        )

    sale_order_id = fields.Many2one(comodel_name="sale.order", string="Sale Order", readonly=True)

    @api.onchange('partner_id')
    def _onchange_partner_id2(self):
        if self.partner_id:
            self.payment_method_id = self.partner_id.payment_method_id

    @api.onchange('sale_order_id')
    def _onchange_sale_order_id(self):
        if self.sale_order_id:
            self.payment_method_id = self.sale_order_id.payment_method_id


class SaleOrder(models.Model):
    _inherit = "sale.order"

    payment_method_id = fields.Many2one(comodel_name="account.journal", string="Payment Method",
                                        required=False, domain=[('type', 'in', ['cash', 'bank'])])

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.payment_method_id = self.partner_id.payment_method_id

    @api.multi
    def _prepare_invoice(self, ):
        """
        Prepare the dict of values to create the new invoice line for a sales order line.

        :param qty: float quantity to invoice
        """
        self.ensure_one()
        res = super(SaleOrder, self)._prepare_invoice()

        res.update({'sale_order_id': self.id})
        if self.payment_method_id:
            res.update({'payment_method_id': self.payment_method_id.id})

        return res


class ResPartner(models.Model):
    _inherit = 'res.partner'

    payment_method_id = fields.Many2one(comodel_name="account.journal", string="Payment Method",
                                        required=False, domain=[('type', 'in', ['cash', 'bank'])])

    @api.onchange('parent_id', 'is_company')
    def _payment_method_onchange_parent_id_individual(self):
        if not self.is_company:
            if self.parent_id:
                self.payment_method_id = self.parent_id.payment_method_id

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ['payment_method_id']
        return res
