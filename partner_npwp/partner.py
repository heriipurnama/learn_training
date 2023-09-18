from odoo import api, fields, models

class partner(models.Model):
    _inherit = 'res.partner'

    npwp = fields.Char(string="NPWP", size=20, required=False)
    property_account_payable_id = fields.Many2one('account.account', company_dependent=True,
        string="Account Payable",
        domain="[('internal_type', '=', 'payable'), ('deprecated', '=', False)]",
        help="This account will be used instead of the default one as the payable account for the current partner",
        required=False)
    property_account_receivable_id = fields.Many2one('account.account', company_dependent=True,
        string="Account Receivable",
        domain="[('internal_type', '=', 'receivable'), ('deprecated', '=', False)]",
        help="This account will be used instead of the default one as the receivable account for the current partner",
        required=False)
    so_ids = fields.One2many(string="Sale Orders",
                             comodel_name="sale.order",
                             inverse_name="partner_id"
                             )
    
    # make and create function
    def create_invoice(self):
        obj_inv = self.env['account.invoice']
        obj_acc = self.env['account.account']

        account = obj_acc.search([('name','=','Product Sales')])
        data = {
            'partner_id': self.id,
            'invoice_line_ids': [
                (0,0,{
                    'name':'Subscription',
                    'quantity':1.0,
                    'price_unit':40,
                    'account_id':account[0].id,
                    }),
                (0,0,{
                    'name':'Management Fee',
                    'quantity':1.0,
                    'price_unit':40,
                    'account_id':account[0].id,
                    }),
            ]
        }
        obj_inv.create(data)
        