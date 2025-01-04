from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval

class OdooPlayGround(models.Model):
    _name = "odoo.playground"
    _description = "Odoo Playground"

    DEFAULT_ENV_VARIABLES = """# Available variables:
# - self: Current object
# - self.env: Odoo environment on which the action is triggered
# - self.env.user: Return the current user (as an instance)
# - self.env.is_system: Return whether the current user is in superuser mode
# - self.env.is_admin: Return whether the current user has group "Settings"
# - self.env.is_superuser: Return whether the environment is in superuser mode
# - self.env.company: Return the current company (as an instance)
# - self.env.companies: Return a recordset of all enabled companies by the user
# - self.env.lang: Return the current language code
"""

    model_id = fields.Many2one('ir.model', string="Model")
    code = fields.Text(string="Code", default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string="Result")

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self

            local_dict = {
                'self': model,
                'env': self.env,
                'user': self.env.user,
            }
            # Evaluate the code safely
            self.result = str(safe_eval(self.code.strip(), local_dict))
        except Exception as e:
            self.result = str(e)