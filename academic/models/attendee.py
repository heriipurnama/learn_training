from odoo import api, fields, models, _


class Attendee(models.Model):
    _name = 'academic.attendee'

    name = fields.Char("Reg. Number", required=True, size=100)
    session_id = fields.Many2one(comodel_name="academic.session",
                                 string="Session")
    partner_id = fields.Many2one(comodel_name="res.partner",
                                 string="Partner")
    
     # check constraint with SQL
    _sql_constraints = [
        ('sql_check_attendee', 'UNIQUE(session_id, partner_id)', 'Atendee Cannot double on one session!')
    ]
    # note: 
    # elm.1: nama contraint
    # elm.2: function contraint
    # elm.3: message