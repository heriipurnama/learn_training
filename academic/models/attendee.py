from odoo import api, fields, models, _


class Attendee(models.Model):
    _name = 'academic.attendee'

    name = fields.Char("Reg. Number", required=True, size=100)
    session_id = fields.Many2one(comodel_name="academic.session",
                                 string="Session")
    partner_id = fields.Many2one(comodel_name="res.partner",
                                 string="Partner")
    # course_id = fields.Many2one(
    #     comodel_name="academic.course",
    #     string="Course")
    # instructor_id = fields.Many2one(
    #     comodel_name="res.partner",
    #     string="Instructor")
    
    # start_date = fields.Date("Start Date")
    # duration = fields.Integer("Duration")
    # seats = fields.Integer("Seats")
    # active = fields.Boolean("is Actice", default=True)
    