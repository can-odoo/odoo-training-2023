from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is property type"

    name = fields.Char(required=True)

