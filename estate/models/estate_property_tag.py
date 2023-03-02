from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Properties Tags'

    name = fields.Char('Property Tags', required=True)

    # sql constraints
    _sql_constraints = [
        ('check_property_tag','UNIQUE(name)', 'The Tag must be unique')
    ]