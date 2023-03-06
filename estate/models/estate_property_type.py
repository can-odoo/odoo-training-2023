from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Types'
    _order = "sequence, name"

    name = fields.Char('Property Types', required=True)
    sequence = fields.Integer('Sequence', help="Used to order stages. Lower is better.")

    property_ids = fields.One2many('estate.property','property_type_id')
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(compute="_offer_count")


    #sql constraints
    _sql_constraints = [
        ('check_property_type','UNIQUE(name)', 'The name must be unique')
    ]

    @api.depends('offer_ids')
    def _offer_count(self):
        for data in self:
            data.offer_count = len(data.offer_ids)