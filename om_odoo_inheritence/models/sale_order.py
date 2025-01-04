from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    name = fields.Char(string='Name' ,required=True)

    def _test_function(self):
        return


    confirm_user_id =fields.Many2one('res.users', string="Confirm user")

    def action_confirm(self):
     super(SaleOrder, self ).action_confirm()
     print("Success.................")
     self.confirm_user_id = self.env.user.id
