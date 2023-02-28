from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

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
    validity = fields.Integer("Validity",default=4)
    date_deadline  = fields.Date("Deadline", compute='_date_deadline', inverse='_inverse_deadline')
    
    @api.depends("create_date","validity")
    def _date_deadline(self):
        for i in self:
            date = i.create_date.date() if i.create_date else fields.Date.today()
            i.date_deadline = date + relativedelta(days=i.validity)
    def _inverse_deadline(self):
        for i in self:
            date = i.create_date.date() if i.create_date else fields.Date.today()
            i.validity = (i.date_deadline - date).days