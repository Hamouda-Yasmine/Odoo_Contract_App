from odoo import api, fields, models


class UnitUsage(models.Model):
    _name = 'contract_management.unit.usage'
    _description = 'Unit Usage'

    name = fields.Char(string=' Name', required=True)