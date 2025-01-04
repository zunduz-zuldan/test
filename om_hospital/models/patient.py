from datetime import date
from traceback import print_list

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital patient"
    _rec_name = 'name'

    name = fields.Char(string='Name', tracking = True)
    date_of_birth =fields.Date(string='Date of Birth')
    ref = fields.Char(string="Reference",default ='Odoo Mates')
    age = fields.Integer(string="Age", compute='_compute_age' , tracking = True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking = True , default='female')
    active = fields.Boolean(string="active", default = True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointments")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")


    @api.model
    def create(self, vals):
        # print("Odoo Mates", vals)
        # # print(".........", self.env['ir.sequence'])
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not  self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        # print("self............", self)
        for rec in self:
            today = date.today()
            # print("today",today)
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1


    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref,record.name)) for record in self]

