# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
    _name = 'g3_bank.account'
    _description = 'Account'

    name = fields.Char()
    balance = fields.Monetary()
    creditLine = fields.Monetary(Required = "False")
    beginBalance = fields.Monetary()
    beginBalanceTimestamp = fields.Date()
    typeAccount = fields.selection()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
