from odoo import models, fields, api

class CustomerDetails(models.Model):
    _name = 'customer.details'
    _description = 'Customer Details'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', default='example@gmail.com')
    phone = fields.Char(string='Phone Number', required=True)
