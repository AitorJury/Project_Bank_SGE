# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
     _name = 'g3_bank.customer'
     _description = 'Customer'
     _inherit = 'res.users'

     #name equivale al campo descripcion
     #name = fields.Char()
     #----------------------
     
     #account_ids=fields.Many2many('g3_bank.account')
