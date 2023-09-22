from odoo import api, fields, models, _


class Session(models.Model):
    _name = 'academic.session'

    name = fields.Char("Name", required=True, size=100)
    course_id = fields.Many2one(
        comodel_name="academic.course",
        string="Course")
    instructor_id = fields.Many2one(
        comodel_name="res.partner",
        string="Instructor")
    
    start_date = fields.Date("Start Date")
    duration = fields.Integer("Duration")
    seats = fields.Integer("Seats")
    active = fields.Boolean("is Actice", default=True)
    