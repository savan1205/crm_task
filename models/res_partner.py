from odoo import fields, models, api


class Partner(models.Model):
    _inherit = "res.partner"
    _description = 'Contacts'

    info_1 = fields.Char(string = "Info 1:")
    info_2 = fields.Char(string = "Info 2:")
    info_3 = fields.Float(string = "Info 3:")