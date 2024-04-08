from odoo import api, fields, models


class UnitSubType(models.Model):
    _name = 'contract_management.unit.subtype'
    _description = 'Subtype for unit'

    name = fields.Char(string=' Name', required=True)