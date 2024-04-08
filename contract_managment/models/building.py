from odoo import api, fields, models

class Building(models.Model):
    _name = 'contract_management.building'
    _description = 'Buildings management'
    
     
    address=fields.Char(string='Address',required=True)
    activity_state = fields.Selection(string='Activity State', selection=[('Overdue', 'overdue'), ('Today', 'today')],required=True)
    name=fields.Char(string='Code',required=True)
    approval_ref_no=fields.Char(string='Approval Ref No',required=True)
    arabic_name=fields.Char(string='Arabic Name',required=True)
    buid_area_size=fields.Float(string="Buid Area (Sq. m)",required=True)
    building_name=fields.Char(string='Building Name',required=True)
    building_type_id=fields.Many2one('contract_management.building.type',String='Building Type',required=True)
    building_usage_ids=fields.Many2many('building.usage',String='Building Usage',required=True)
    project_id=fields.Many2one('contract_management.project' ,required=True ,string='Project ID')

    city_id=fields.Many2one('res.city',string='Area',required=True)
    commom_area_size=fields.Float(string='Commom Area (Sq. m)',required=True)
    completion_date=fields.Date(string='Completion Date',required=True)
    ejari_building_area_size=fields.Float(string='Ejari Building Area (Sq. m)',required=True)
    ejari_building_name=fields.Char(string='Ejari Building Name',required=True)
    ejari_building_name_arabic=fields.Char(string='Ejari Building Name Arabic',required=True)
    ejari_common_area_size=fields.Float(string='Ejari Common Area (Sq. m)',required=True)
    ejari_leasable_area_size=fields.Float(string='Ejari Leasable Area (Sq. m)',required=True)
    floor_count=fields.Integer(string='Floor Count',required=True)
    hold_type_id=fields.Selection([('free','Free Hold'),
                                   ('nonfree','Non Free Hold')
                                   ],string='Hold Type',required=False)
    land_no_id=fields.Char(string='Land No',required=True)
    leasable_area_size=fields.Float(string='Leasable Area (Sq. m)',required=True)
    active = fields.Boolean(string='Active',default=False)
    state_id=fields.Many2one('res.country.state',string="Emirate",required=True)