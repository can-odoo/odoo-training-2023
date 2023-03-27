from odoo import fields, models
from odoo.exceptions import UserError

class cardekhowizard(models.TransientModel):
    _name = "cardekho.wizard"

    price = fields.Float("Price")
    partner_id = fields.Many2one("res.partner", required=True)

    def make_offers(self):
        active_records = self.env.context.get('active_ids')
        for record in active_records:
            property_id = self.env['car.dekho.property'].browse(record)
            if property_id.state != "offer_accepted":
                property_id.write({
                    "offer_ids": [
                        fields.Command.create({
                            "price": self.price,
                            "partner_id": self.partner_id.id,
                        })
                    ]
                })
        else:
            raise UserError(
                "Offer not put's on properties whoes state is accepted")
