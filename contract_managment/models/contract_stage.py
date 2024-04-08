from odoo import api, fields, models


class ContractStage(models.Model):
    _name = 'contract_management.contract.stage'
    _description = 'Stage of contract'

    name = fields.Char(string=' Name', required=True)