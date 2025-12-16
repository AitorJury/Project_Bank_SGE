# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
     _name = 'g3_bank.customer'
     _description = 'Customer'

     #name equivale al campo descripcion
     #name = fields.Char()
     #----------------------
     first_name = fields.Char(required=True)
     last_name = fields.Char(required=True)
     middle_name = fields.Char(required=True)
     street = fields.Char(required=True)
     city = fields.Char(required=True)
     state = fields.Char(required=True)
     zip = fields.Integer(required=True)
     phone = fields.Integer(required=True)
     email = fields.Char(required=True)
     password = fields.Char(required=True)
     account_ids=fields.Many2many('g3_bank.account')
