from odoo import api, fields, models


class BuildingType(models.Model):
    _name = 'contract_management.building.type'
    _description = 'Types of buildings'

    name = fields.Char(string=' Name', required=True)


