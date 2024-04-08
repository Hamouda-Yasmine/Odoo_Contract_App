from odoo import api, fields, models

class Project(models.Model):
    _name = 'contract_management.project'
    _description = 'Project managment'

    name = fields.Char(string='Code',required=True)
    owner = fields.Many2one('res.partner',string='Owner',required=True)
    managed_by = fields.Many2one('res.partner',string='Managed By',required=True)
    maintained_by = fields.Many2one('res.partner',string="Maintained By",required=True)
    active = fields.Boolean(string='Active',default=False)
    state_id=fields.Many2one('res.country.state',string="Emirate",required=True)
    
    
   
