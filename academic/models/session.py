from odoo import api, fields, models, _
import time

# make Global Variabel
STATES = [('draft','Draft'),
         ('confirmed','Confirmed'),
         ('done','Done')]
class Session(models.Model):
    _name = 'academic.session'

    name = fields.Char("Name", 
                       required=True, 
                       size=100, 
                       readonly=True, 
                       STATES={'draft':[{'readonly', False}]}
                       )
    # readonly true but if STATES 'draft' readonly = FALSE.
    course_id = fields.Many2one(
        comodel_name="academic.course",
        string="Course",
        readonly=True, 
        STATES={'draft':[{'readonly', False}]})
    
    instructor_id = fields.Many2one(
        comodel_name="res.partner",
        readonly=True, 
        STATES={'draft':[{'readonly', False}]},
        string="Instructor")
    
    start_date = fields.Date("Start Date", default=lambda self: time.strftime("%Y-%m-%d"),
                              readonly=True, 
                              STATES={'draft':[{'readonly', False}]})
    duration = fields.Integer("Duration",
                               readonly=True, 
                               STATES={'draft':[{'readonly', False}]})
    seats = fields.Integer("Seats",
                            readonly=True, 
                            STATES={'draft':[{'readonly', False}]})
    active = fields.Boolean("is Actice", default=True,
                             readonly=True, 
                             STATES={'draft':[{'readonly', False}]})
    
    attendee_ids = fields.One2many(comodel_name="academic.attendee",
                                   string="Attendees",
                                   inverse_name="session_id",
                                   readonly=True, 
                                   STATES={'draft':[{'readonly', False}]})
    
    taken_seats = fields.Float(string="Taken Seats",
                                compute="_taken_seats",
                                readonly=True)
    
    image_small = fields.Binary("Image",
                                 readonly=True, 
                                 STATES={'draft':[{'readonly', False}]})
   
    def _taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids)/ rec.seats
            else:
                rec.taken_seats = 0.0
    
    @api.onchange('seats')
    def onChange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids)/ self.seats
        else:
            self.taken_seats = 0.0

    def check_instructor(self):
        # contraint with python script!
        for session in self:
        # metode 1
        #    a = []
        #    for attendee in session.attendee_ids:
        #        a.append(attendee.partner_id.id)

        # metode 2
            a = [attendee.partner_id.id for attendee in session.attendee_ids]
            if session.instructor_id.id in a:
                return False   
        return True

    _constraint = [(check_instructor,'Instruktur Tidak Boleh Merangkap jadi Attendee',['instructor_id', 'attendee_ids'])]
    # note: nama topel python
    # elm.1: nama fungsi
    # elm.2: message
    # elm.3: list field-field yg mau di seteksi inputan

    # method copy to duplicated form.
    def copy(self, default=None):
        # modif....
        print("default==> ", default)
        self.ensure_one()
        default = dict(default or {},
                       name=_('Copy of %s') % self.name)
        return super(Session, self).copy(default=default)
        
    # make workflow
    state = fields.Selection(
            string="State",
            selection=STATES,
            readonly=True,
            required=True,
            default=STATES[0][0]
        )
    
    def action_confirm(self):
        self.state = STATES[1][0]

    def action_done(self):
        self.state = STATES[2][0]
    
    def action_draft(self):
        self.state = STATES[0][0]
        