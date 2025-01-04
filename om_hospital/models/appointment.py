from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string="patient")
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    ref = fields.Char(string='Reference' ,
                      help="Reference of the patient from patient record")
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date =fields.Date(string='Booking_date', default=fields.Date.today)
    prescription = fields.Html(string='prescription')
    priority = fields.Selection([
        ( '0' ,'Normal'),
          ('1','Low'),
          ('2','High'),
          ('3','Very High')], string="Priority",
          help='Gives the sequence oder when displaying a list of MRP documents.')
    state = fields.Selection([
         ('draft', 'Draft'),
         ('in_consultation', 'In Consultation'),
         ('done', 'Done'),
         ('cancel', 'Cancelled')], default='draft', string = "Status",required=True)
    doctor_id = fields.Many2one('res.users',string='Doctor', tracking=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='pharmacy Lines')
    hide_sales_price = fields.Boolean(string="Hide sales price")


    @api.onchange(' patient_id')
    def onchange_patient_id(self):
        self.ref = self. patient_id.ref

    def action_test(self):
        print("Button clicked !!!!!!!!!!!")

        return {
        'effect': {
            'fadeout': 'slow',
            'message': 'Click Successful',
            'type': 'rainbow_man',
             }
           }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
       for rec in self:
            rec.state = 'draft'


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = "Appointment Pharmacy Lines"
    product_id =fields.Many2one('product.product',required=True)
    price_unit =fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
