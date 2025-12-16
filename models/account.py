# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models


class Account(models.Model):
    _name = 'g3_bank.account'
    _description = 'Account'

# Enumeración para el campo typeAccount
    TYPE_ACCOUNT_SELECTION = [
        ('STANDARD', 'Standard'),
        ('CREDIT', 'Credit'),
    ]

#   El id no se define, Odoo lo añade automáticamente
#   Utilizo name como la descripción de Account
    name = fields.Char(string='Description', required=True)
    balance = fields.Double(string='Balance', required=True)
    creditLine = fields.Double(string='Credit Line', required=True)
    beginBalance = fields.Double(string='Begin Balance', required=True)
    beginBalanceTimestamp = fields.Date(string='Begin Balance Timestamp', required=True)
    # La selección del tipo de cuenta
    typeAccount = fields.Selection(selection=TYPE_ACCOUNT_SELECTION, string='Account Type', required=True)
    
#   Relación con Customer (Muchos a Muchos)
    customer_ids = fields.Many2many('g3_bank.customer', string='Customers')
#   Relación con Movement (Uno a Muchos)
    movement_ids = fields.One2many(
        'g3_bank.movement', 
        'account_id',
        ondelete='cascade',
        string='Movements'
    )

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
