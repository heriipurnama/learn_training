from odoo import api, fields, models, _


class Course(models.Model):
    _name = 'academic.course'

    name = fields.Char("Name", required=True, size=100)
    description = fields.Text("Description", required=True)
    responsible_id = fields.Many2one(
        comodel_name="res.users", 
        string="Responsible",
        required=True)
    
    session_ids = fields.One2many(
            comodel_name="academic.session",
            string="sessions",
            inverse_name="course_id"
        )
    
    # check constraint with SQL
    _sql_constraints = [
        ('sql_check_name', 'UNIQUE(name)', 'Duplicate Name!'),
        ('sql_check_description','CHECK(name <> description)', 'Name and description cannot be same!')
    ]
    # note: 
    # elm.1: nama contraint
    # elm.2: function contraint
    # elm.3: message