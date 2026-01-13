# -*- coding: utf-8 -*-

import enum
from odoo import api, fields, models

class Account(models.Model):
    _name = 'g3_bank.account'
    _description = 'Account'

#   El id no se define, Odoo lo añade automáticamente
#   Utilizo name como la descripción de Account
    name = fields.Char(string='Description', required=True)
    balance = fields.Float(string='Balance', default=0.0)
    creditLine = fields.Float(string='Credit Line', default=0.0)
    beginBalance = fields.Float(string='Begin Balance', required=True)
    beginBalanceTimestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now)
    # La selección del tipo de cuenta
    typeAccount = fields.Selection([
        ('STANDARD', 'Standard'),
        ('CREDIT', 'Credit'),
    ], string='Account Type', required=True, default='STANDARD')
    
#   Relación con Customer (Muchos a Muchos)
    customer_ids = fields.Many2many('res.users', string='Customers')
#   Relación con Movement (Uno a Muchos)
    movement_ids = fields.One2many('g3_bank.movement', 'account_id', string='Movements')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
