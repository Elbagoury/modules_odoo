# -*- coding: utf-8 -*-
from odoo import http

# class LocalinkMailTemplate(http.Controller):
#     @http.route('/localink_mail_template/localink_mail_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/localink_mail_template/localink_mail_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('localink_mail_template.listing', {
#             'root': '/localink_mail_template/localink_mail_template',
#             'objects': http.request.env['localink_mail_template.localink_mail_template'].search([]),
#         })

#     @http.route('/localink_mail_template/localink_mail_template/objects/<model("localink_mail_template.localink_mail_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('localink_mail_template.object', {
#             'object': obj
#         })