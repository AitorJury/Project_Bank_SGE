# -*- coding: utf-8 -*-

import enum
from odoo import api, fields, models

class Account(models.Model):
    _name = 'g3_bank.account'
    _description = 'Account'

# Campo técnico necesario para Monetary
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                  default=lambda self: self.env.company.currency_id)

#   El id no se define, Odoo lo añade automáticamente
#   Utilizo name como la descripción de Account
    name = fields.Char(string='Description', required=True)
    balance = fields.Monetary(string='Balance', currency_field='currency_id', default=0.0)
    creditLine = fields.Monetary(string='Credit Line', currency_field='currency_id', default=0.0)
    beginBalance = fields.Monetary(string='Begin Balance', currency_field='currency_id', required=True)
    beginBalanceTimestamp = fields.Datetime(string='Opening Date', default=fields.Datetime.now)
    # La selección del tipo de cuenta
    typeAccount = fields.Selection([
        ('STANDARD', 'Standard'),
        ('CREDIT', 'Credit'),
    ], string='Account Type', required=True, default='STANDARD')
    
#   Relación con Customer (Muchos a Muchos)
    customer_ids = fields.Many2many('g3_bank.customer', string='Customers')
#   Relación con Movement (Uno a Muchos)
    movement_ids = fields.One2many('g3_bank.movement', 'account_id', string='Movements')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
