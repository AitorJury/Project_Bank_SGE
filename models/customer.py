# -*- coding: utf-8 -*-
import re
from xml.dom import ValidationErr

from odoo.exceptions import ValidationError
from odoo import models, fields, api


EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class Customer(models.Model):
     #_name = 'g3_bank.customer'
     _description = 'Customer'
     _inherit = 'res.users'

     #name equivale al campo descripcion
     #name = fields.Char()
     #----------------------

     account_ids=fields.Many2many('g3_bank.account')
     # users_ids=fields.Many2many('res.users')


     # @api.constrains('login')
     # def _check_email_format(self):
     #     for record in self:
     #         #Comprobar que el email cumpla con el formato
     #         if record.login and not re.fullmatch(EMAIL_PATTERN, record.login) :
     #             raise ValidationError('El email debe tener el formato ')
     #
     # @api.onchange('login')
     # def onchange_email(self):
     #    if self.login and not re.fullmatch(EMAIL_PATTERN, self.login):
     #        return {
     #            'warning': {
     #                'title': 'Email invalido',
     #                'message': 'El email debe tener el formato '
     #            }
     #        }

     @api.constrains('zip')
     def _check_zip_format(self):
         for record in self:
             #Comprobar que el zip cumpla con el formato
             if record.zip and not record.zip.isdigit():
                 raise ValidationError('El código postal (ZIP) solo debe contener números.')
             if len(record.zip) != 5:
                 raise ValidationError('El código postal debe tener exactamente 5 dígitos.')
             if len(record.zip) < 0:
                 raise ValidationError('El codigo postal deber estar relleno')


     @api.onchange('zip')
     def onchange_zip(self):
         if self.zip:
             # Usamos regex para verificar que sean exactamente 5 números
             if not re.fullmatch(r'^\d{5}$', self.zip):
                 return {
                     'warning': {
                         'title': 'Código Postal no válido',
                         'message': 'El ZIP debe tener exactamente 5 dígitos numéricos (ejemplo: 28001).'
                     }
                 }

     # @api.onchange('zip')
     # def onchange_zip(self):
     #    if self.zip and not re.fullmatch('^[0-9]+$', self.zip):
     #        return {
     #            'warning': {
     #                'title': 'zip invalido',
     #                'message': 'El zip debe tener el formato '
     #            }
     #        }
