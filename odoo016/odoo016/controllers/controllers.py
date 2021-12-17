# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo016(http.Controller):
#     @http.route('/odoo016/odoo016/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo016/odoo016/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo016.listing', {
#             'root': '/odoo016/odoo016',
#             'objects': http.request.env['odoo016.odoo016'].search([]),
#         })

#     @http.route('/odoo016/odoo016/objects/<model("odoo016.odoo016"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo016.object', {
#             'object': obj
#         })
