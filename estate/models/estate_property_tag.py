from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is property tag"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    _sql_constraints = [ ('check_property_tag','UNIQUE (name)','Property Tag should be unique')]