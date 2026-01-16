# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movement(models.Model):
    _name = 'g3_bank.movement'
    _description = 'Movement'
    
    name = fields.Char(string = "Description", required = True)
    timestamp = fields.Datetime(string = "TimeStamp", required = True, default=fields.Datetime.now)
    amount = fields.Float(String = "Amount", default=0.0)
    balance = fields.Float(String = "Balance", default=0.0)
    
    account_id = fields.Many2one('g3_bank.account', string="Account")
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
