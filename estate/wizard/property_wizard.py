from odoo import models,fields

class PropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"

    def get_active(self):
        return self.env['estate.property'].browse(self._context.get('active_ids'))

    price = fields.Float()
    buyer = fields.Many2one('res.partner')
    validity = fields.Integer("Validity ( days )",default=7)
    property_ids = fields.Many2many('estate.property',default=get_active)

    def create_offer(self):
        for offer in self:
            for record in offer.property_ids:
                if record.best_offer<=offer.price:
                    self.env['estate.property.offer'].create({
                    'price':offer.price,
                    'partner_id':offer.buyer.id,
                    'property_id':record.id,
                    'validity':offer.validity
                    })
                print(offer.validity)