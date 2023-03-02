from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Types'

    name = fields.Char('Property Types', required=True)

    #sql constraints
    _sql_constraints = [
        ('check_property_type','UNIQUE(name)', 'The name must be unique')
    ]