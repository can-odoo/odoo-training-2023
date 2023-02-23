from odoo import fields, models

class carOffers(models.Model):
    _name="cardekho.property.offer"
    _description="Car offer"

    price = fields.Float("Price", required=True)
    state = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
        default=False,
    )
    partner_id = fields.Many2one("res.partner", string="Offer From", required=True)
    car_id = fields.Many2one("car.dekho.property", string="CarId", required=True)