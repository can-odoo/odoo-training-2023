from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type" 
    _order = "name , sequence"

    name = fields.Char('Property Type' , required=True)
    properties_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
    sequence = fields.Integer('Sequence')

    _sql_constraints = [
        ('unique_property_type', 'UNIQUE(name)', 'Property Type already exists.')
    ]