# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pagos(models.Model):
    _name = 'odoo_testing.pagos'

    name =      fields.Char(required=True, help = 'Nombre de cliente')
    telefono    = fields.Integer(required=True, help = 'telefono del cliente en formato 6560123123')
    email       = fields.Char(help = 'correo electronico, opcional')
    costoTotal  = fields.Float(compute="_value_pc", store=True, required = True, help = 'Adeudo inicial del viaje')
    description = fields.Text(help = 'datos generales del cliente')
    direccion   = fields.Text(required = True, help = 'Direccion del cliente')
    viaje       = fields.Char(required = True, help = 'Viaje que compra')

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100

class Viajes(models.Model):
    _name = 'odoo_testing.viaje'

    name = fields.Char(required = True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string='Number of seats')

