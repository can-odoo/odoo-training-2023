from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property type are defined"
    _order = "sequence, name"
 
    name = fields.Char('Property Type',required=True)
    property_ids = fields.One2many('estate.recurring.plan','property_type_id',string='Properties')
    sequence = fields.Integer('Sequence', default=10)
    _sql_constraints = [('Typename','UNIQUE(name)','Property type name must be unique')]
    