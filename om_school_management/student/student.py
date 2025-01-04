from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age= fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number', required=True)
