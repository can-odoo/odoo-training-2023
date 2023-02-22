from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is property tag"

    name = fields.Char(required=True)