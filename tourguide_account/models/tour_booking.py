from odoo import fields, models, Command

class TourBooking(models.Model):
    _inherit='tour.booking'

    def action_to_confirm(self):
        print("invoice generate")
        self.env["account.move"].create(
            {
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                        "name": "customer",
                        "quantity": 1,
                        "price_unit": self.total_cost
                    }),
                    Command.create({
                        "name": "Administrative Fees",
                        "quantity": 1,
                        "price_unit": 100
                    })
                ]
            }
        )
        return super(TourBooking, self).action_to_confirm()