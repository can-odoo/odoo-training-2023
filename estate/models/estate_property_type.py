from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type" 

    name = fields.Char('Property Type' , required=True)

    _sql_constraints = [
        ('unique_property_type', 'UNIQUE(name)', 'Property Type already exists.')
    ]