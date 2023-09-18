from odoo import api, fields, models, _


class Course(models.Model):
    _name = 'academic.course'

    name = fields.Char("Name", required=True, size=100)
    description = fields.Text("Description", required=True)
    responsible_id = fields.Many2one(
        comodel_name="res.users", 
        string="Responsible",
        required=True)
    