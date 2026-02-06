from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

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
    balance = fields.Monetary(related='account_id.balance', string="Balance", currency_field='currency_id', default=0.0, readonly=True)
    
    #Ponemos un campo relacional que lo coge desde cuentas para poder ver el credito 
    credit_limit_info = fields.Monetary(related='account_id.creditLine', string="Account Credit")
    account_type = fields.Selection(related='account_id.typeAccount')
    
    credit_available = fields.Monetary(
                                       string="Credit ", 
                                       compute="_compute_credit_available",
                                       currency_field='currency_id'
                                       )
    
    
    account_id = fields.Many2one('g3_bank.account', string="Account", readonly=True)
    
    # En models/movement.py
    
    @api.constrains('amount', 'name', 'account_id')
    def _validationAmountError(self):
        for r in self:
            if r.amount <= 0:
                raise ValidationError("The amount must be greater than 0.")
        
            if r.name == 'payment':
                total_disponible = r.account_id.balance + r.account_id.creditLine
            
                if r.amount > total_disponible:
                    raise ValidationError("The balance and credit are insufficient.")
            
                if r.amount > r.account_id.balance:
                    credit_necesario = r.amount - r.account_id.balance
                    r.account_id.creditLine -= credit_necesario
                    
                    