# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
     _name = 'g3_bank.customer'
     _description = 'Customer'
     _inherits = {'res.users': 'user_id'}

     #name equivale al campo descripcion
     #name = fields.Char()
     #----------------------
     user_id = fields.Many2one('res.users', string='Related User', 
                              required=True, ondelete='cascade')

     account_ids=fields.Many2many('g3_bank.account', string='Accounts')
     # users_ids=fields.Many2many('res.users')
