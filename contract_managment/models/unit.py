from odoo import api, fields, models

class Unit(models.Model):
    _name = 'contract_management.unit'
    _description = 'Unit managment'

    name = fields.Char(string='Name', required=True)
    floor_no=fields.Char(string='Floor NO', required=True)
    active=fields.Boolean(string='Active', required=True)
    approval_ref_no=fields.Char(string='Approval Ref No', required=True)
    building_id=fields.Many2one('contract_management.building', string='Building', required=True)
    common_area_size=fields.Float(string='Common Area (Sq. m)', required=True)
    reference_no=fields.Char(string='Property Reference No', required=True)
    status=fields.Selection([('approved', 'approved')], string='Status', required=True)
    suit_area_size=fields.Float(string='Suit Area (Sq. m)', required=True)
    total_area_size=fields.Float(string='Total Area (Sq. m)',required=True)
    unit_no=fields.Char(string=' Unit No', required=True)
    unit_subtype_id=fields.Many2one('contract_management.unit.subtype', string='Unit Subtype')
    unit_type_id=fields.Many2one('contract_management.unit.type', string=' Unit Type', required=True)
    unit_usage_id=fields.Many2one('contract_management.unit.usage', string=' Unit Usage', required=True)

    
    