from odoo import fields, models

class PropertyType(models.Model):
    _name = "cardekho.property.type"
    _description = "Car property described here"

    name = fields.Char('Car type',required=True)
    