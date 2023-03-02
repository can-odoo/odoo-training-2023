from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is property tag"

    name = fields.Char(required=True)

    _sql_constraints = [ ('check_property_tag','UNIQUE (name)','Property Tag should be unique')]