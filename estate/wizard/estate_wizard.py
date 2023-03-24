from odoo import fields, models

class estatewizard(models.TransientModel):
    _name = "estate.wizard"

    price = fields.Float("Price")
    partner_id = fields.Many2one("res.partner", required=True)

    def make_offers(self):
        print("*******", self.env.context)
        active_records = self.env.context.get('active_ids')
        for record in active_records:
            property_id = self.env['estate.recurring.plan'].browse(record)
            property_id.write({
                "offer_ids":[
                    fields.Command.create({
                        "price" : self.price,
                        "partner_id" : self.partner_id.id,
                    })
                ]
            })
            