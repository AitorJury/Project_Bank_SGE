# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movement(models.Model):
    _name = 'g3_bank.movement'
    _description = 'Movement'
    
    # Campo técnico necesario para Monetary
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                  default=lambda self: self.env.company.currency_id)

    name = fields.Char(string = "Description", required = True)
    timestamp = fields.Datetime(string = "TimeStamp", required = True, default=fields.Datetime.now)
    amount = fields.Monetary(string = "Amount", currency_field='currency_id', default=0.0)
    balance = fields.Monetary(string = "Balance", currency_field='currency_id', default=0.0)
    
    #account_id = fields.Many2one('g3_bank.account', string="Account")
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
