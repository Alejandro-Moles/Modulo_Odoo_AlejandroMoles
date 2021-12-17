# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo016(models.Model):
#     _name = 'odoo016.odoo016'
#     _description = 'odoo016.odoo016'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100





from odoo import models, fields, api

class usuario(models.Model):
	_name = 'odoo016.usuario'
	_description = 'model usuario'

	name = fields.Char('NombreUsuario',required=True,unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
	edad = fields.Integer(string="Edad",required=True)
    



	