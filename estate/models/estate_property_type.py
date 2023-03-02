from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property type are defined"

    name = fields.Char('Property Type',required=True)
    _sql_constraints = [('Typename','UNIQUE(name)','Property type name must be unique')]
    