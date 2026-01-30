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
    balance = fields.Monetary(string="Balance", currency_field='currency_id', default=0.0, readonly=True, compute="_compute_movement_balance")
    
    account_id = fields.Many2one('g3_bank.account', string="Account", readonly=True)
    
    @api.constrains('amount', 'name', 'account_id')
    def _validationAmountError(self):
        for r in self:
            # Valido que el amount sea positivo
            if r.amount <= 0:
                #Si no salta la excepcion
                raise ValidationError("The amount must be greater than 0.")
            
            #Valido que el dinero al hacer un pago sea mayor que el balance
            if r.name == 'payment':
                if r.amount > r.account_id.balance:
                    raise ValidationError("You do not have enough money in account")
                
    @api.depends('amount', 'name', 'account_id.balance')
    def _compute_movement_balance(self):
        for r in self:
            # Primero cogemos el balance actual de la cuenta
            current_account_balance = r.account_id.balance         
            if r.name == 'payment':
                r.balance = current_account_balance - r.amount
            elif r.name == 'deposit':
                r.balance = current_account_balance + r.amount
            else:
                r.balance = current_account_balance