from odoo import api, fields, models


class Contract(models.Model):
    _name = 'contract_management.contract'
    _description = 'Contract management'

    active = fields.Boolean(string='Active', default=False)
    company_id = fields.Many2one('res.partner', string='Owner', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    #date = fields.Date(string='Date', required=True)
    date_start = fields.Date(string='Date Start', required=True)
    date_stop = fields.Date(string='Date Stop', required=True)
    kanban_state = fields.Selection([('normal', 'In Progress'),
                                     ('done', 'Approved'),
                                     ('blocked', 'Blocked')], string='Kanban')
    name = fields.Char(string='Code', required=True)
    notes = fields.Text(string='Notes', required=True)
    user_id = fields.Many2one('res.users', string='User')
    partner_id = fields.Many2one('res.partner', string='Tenant')
    period = fields.Selection([('month', 'Months'), ('year', 'Years')], string='Period')
    period_nbr = fields.Integer(string='Period Nbr')
    stage_id = fields.Many2one('contract_management.contract.stage', string='Stage')
    unit_id = fields.Many2one('contract_management.unit', string='Unit', required=True ,)



    def confirm_contract(self):
        self.unit_id.reserved = True

                
