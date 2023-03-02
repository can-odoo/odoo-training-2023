from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is property type"

    name = fields.Char(required=True)

    _sql_constraints = [ ('check_property_type','UNIQUE (name)','Property Type should be unique')]