from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is property type"
    _order = "sequence,name"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('Sequence')

    _sql_constraints = [ ('check_property_type','UNIQUE (name)','Property Type should be unique')]