from odoo import fields, models
from odoo import Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'


    def action_to_sold(self):
        print("invoice is created")
        x = super(EstateProperty, self).action_to_sold()
        self.env["account.move"].create(
            {
                'partner_id': self.buyer_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                        'name': 'Brokerage',
                        'quantity': 1,
                        'price_unit': self.selling_price*0.06
                    }),
                    Command.create({
                        'name': 'Administrative fees',
                        'quantity': 1,
                        'price_unit': 100
                    })
                ]
        })
        return x