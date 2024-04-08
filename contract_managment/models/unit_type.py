from odoo import api, fields, models


class UnitType(models.Model):
    _name = 'contract_management.unit.type'
    _description = 'Type for unit'

    name = fields.Char(string=' Name', required=True)