from multiprocessing import context
from odoo import api, fields, models, _

class AttendeeWizard(models.TransientModel):
    _name = "academic.attendee.wizard"

    def _get_default_session(self):
        context = self.env.context
        if context.get('active_model') == 'academic.session':
            return context.get('active_ids', False)
        
        return False

    # one record
    session_id = fields.Many2one(
            comodel_name="academic.session",
            string="Session",
            default =  _get_default_session
        )
    
    # multi record
    # session_ids = fields.Many2many(
    #       comodel_name="academic.session",
    #       string="Session(s)",
    #       default =  _get_default_session
    #   )
    

    attendee_ids = fields.One2many(
        comodel_name= "academic.attendee.wizard.partner",
        inverse_name= "wizard_id",
        string="Parnerts to add"
    )

    # after process succes than close the windows wizard / popUp
    def action_add_attendee(self):
        # debug method
        import pdb; pdb.set_trace()

        self.ensure_one()

        # ......
        session_id = self.session_id
        # looping attendee
        # inset to session attendee)ids one2many

        #  [10,11,13] =>
        #  list comprehensions [(0,0,{name='',partner_id:10}),(0,0,{partner_id:11}),(0,0,{partner_id:13})]
        # one record
        session_id.attendee_ids = [ 
            (0,0,{'name':'001', 'partner_id': x.partner_id.id}) for x in self.attendee_ids
        ]

        # multi record
        # for session_id in session_ids :
        #     session_id.attendee_ids = [ 
        #         (0,0,{'name':'001', 'partner_id': x.partner_id.id}) for x in self.attendee_ids
        #     ]

        return {'type': 'ir.action.act_window_close '}

class AttendeePartner(models.TransientModel):
    _name = "academic.attendee.wizard.partner"

    wizard_id = fields.Many2many(
        comodel_name="academic.attendee.wizard",
        string="wizard"
    )

    partner_id = fields.Many2many(
        comodel_name="res.partner",
        string="Partner to add "
    )

