from odoo import models,fields,api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "This is property type"
    _order = "sequence,name"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('Sequence')
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer('Offer count',compute = "_compute_offer")

    @api.depends('offer_ids')
    def _compute_offer(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    _sql_constraints = [ ('check_property_type','UNIQUE (name)','Property Type should be unique')]