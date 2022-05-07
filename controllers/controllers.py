# -*- coding: utf-8 -*-
# from odoo import http


# class AccountBoliviaLectorQr(http.Controller):
#     @http.route('/account_bolivia_lector_qr/account_bolivia_lector_qr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_bolivia_lector_qr/account_bolivia_lector_qr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_bolivia_lector_qr.listing', {
#             'root': '/account_bolivia_lector_qr/account_bolivia_lector_qr',
#             'objects': http.request.env['account_bolivia_lector_qr.account_bolivia_lector_qr'].search([]),
#         })

#     @http.route('/account_bolivia_lector_qr/account_bolivia_lector_qr/objects/<model("account_bolivia_lector_qr.account_bolivia_lector_qr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_bolivia_lector_qr.object', {
#             'object': obj
#         })
