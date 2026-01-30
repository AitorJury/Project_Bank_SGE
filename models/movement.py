from odoo import api
from odoo import fields
from odoo import models


class Movement(models.Model):
    _name = 'g3_bank.movement'
    _description = 'Movement'
    
    # Campo técnico necesario para Monetary
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                  default=lambda self: self.env.company.currency_id)

    name = fields.Selection([
                            ('payment', 'Payment'),
                            ('deposit', 'Deposit')
                            ], string="Description", required=True)
                            
    timestamp = fields.Datetime(string="Date", required=True, default=fields.Datetime.now, readonly=True)
    amount = fields.Monetary(string="Amount", currency_field='currency_id', default=0.0)
    balance = fields.Monetary(string="Balance", currency_field='currency_id', default=0.0 , readonly =True)
    
    account_id = fields.Many2one('g3_bank.account', string="Account")
    
    
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100