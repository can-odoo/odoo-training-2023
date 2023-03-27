from odoo import fields, models

class SetOffer(models.TransientModel):
    _name = 'set.offer'
    _description = 'Set Offer'

    price = fields.Float('price')
    partner_id = fields.Many2one('res.partner', required=True)

    def action_to_make_offer(self):
        property = self.env['estate.property'].browse(self._context.get('active_ids'))
        for record in self:
            for data in property:
                self.env['estate.property.offer'].create({
                    'price' : record.price,
                    'partner_id' : record.partner_id.id,
                    'property_id' : data.id
                })