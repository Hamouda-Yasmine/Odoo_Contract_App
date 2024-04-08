from odoo import api, fields, models


class BuildingUsage(models.Model):
    _name = 'building.usage'
    _description = 'Usage of buildings'

    name = fields.Char(string=' Name', required=True)


