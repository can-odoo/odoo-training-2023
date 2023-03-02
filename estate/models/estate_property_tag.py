from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'

    name = fields.Char('Property Tags', required=True)

    _sql_constraints = [
        ('unique_property_tag', 'UNIQUE(name)', 'Property Tag already exists.')
    ]