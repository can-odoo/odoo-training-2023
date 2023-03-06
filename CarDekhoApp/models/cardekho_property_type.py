from odoo import fields, models, api

class PropertyType(models.Model):
    _name = "cardekho.property.type"
    _description = "Car property described here"
    _order="name"

    name = fields.Char('Car type',required=True)
    property_ids = fields.One2many('car.dekho.property','car_property_id',string='Properties')
    offer_ids = fields.One2many('cardekho.property.offer','car_property_id',string='Offers')
    offer_count = fields.Integer(compute="_count_offer", string='Offer Count')
    _sql_constraints = [('Typename','UNIQUE(name)','Car type name must be unique')]

    @api.depends("offer_ids")
    def _count_offer(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
