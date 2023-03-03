from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Types'
    _order = "sequence, name"

    name = fields.Char('Property Types', required=True)
    sequence = fields.Integer('Sequence', help="Used to order stages. Lower is better.")

    property_ids = fields.One2many('estate.property','property_type_id')

    #sql constraints
    _sql_constraints = [
        ('check_property_type','UNIQUE(name)', 'The name must be unique')
    ]