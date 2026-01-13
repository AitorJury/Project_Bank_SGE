# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movement(models.Model):
    _name = 'g3_bank.movement'
    _description = 'Movement'
    
    name = fields.Char(string = "Description", required = True)
    timestamp = fields.DateTime(string = "TimeStamp", required = True, default=fields.Datetime.now)
    amount = fields.Monetary(String = "Amount", required = True)
    balance = fields.Monetary(String = "Balance", required = True)
    
    account_id = fields.Many2one('g3_bank.account', string="Account")
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
