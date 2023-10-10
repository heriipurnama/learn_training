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
    
    attendee_ids = fields.One2many(comodel_name="academic.attendee",
                                   string="Attendees",
                                   inverse_name="session_id")
    
    taken_seats = fields.Float(string="Taken Seats",
                               compute="_taken_seats")
   
    def _taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids)/ rec.seats
            else:
                rec.taken_seats = 0.0
    
    @api.onchange('seats')
    def oChange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids)/ self.seats
        else:
            self.taken_seats = 0.0
