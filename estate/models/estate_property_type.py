from odoo import fields, models, api

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property type are defined"
    _order = "sequence, name"
 
    name = fields.Char('Property Type',required=True)
    property_ids = fields.One2many('estate.recurring.plan','property_type_id',string='Properties')
    sequence = fields.Integer('Sequence', default=10)
    offer_ids = fields.One2many('estate.property.offer','property_type_id', string='Offers')
    offer_count=fields.Integer(compute="_count_offers", string='Offer Count')
    _sql_constraints = [('Typename','UNIQUE(name)','Property type name must be unique')]    

    @api.depends('offer_ids')
    def _count_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)