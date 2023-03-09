from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class carOffers(models.Model):
    _name="cardekho.property.offer"
    _description="Car offer"
    _order="price desc"

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
    car_property_id = fields.Many2one(related='car_id.car_property_id',store=True,string='Property Type')
    _sql_constraints = [('OfferPrice','CHECK(price > 0)','Offer price must be positive')]
    
    @api.depends("create_date","validity")
    def _date_deadline(self):
        for i in self:
            date = i.create_date.date() if i.create_date else fields.Date.today()
            i.date_deadline = date + relativedelta(days=i.validity)
    def _inverse_deadline(self):
        for i in self:
            date = i.create_date.date() if i.create_date else fields.Date.today()
            i.validity = (i.date_deadline - date).days

    def accept_state(self):
        self.write({'state':'accepted'})
        return self.mapped("car_id").write({'state':'offer_accepted',
                                            'buyer_id':self.partner_id.id,
                                            'selling_price':self.price
                                          })
    def refused_state(self):
        self.write({'state':'refused'})


    #pyhton inheritance
    @api.model
    def create(self,vals):
        if vals.get('car_id') and vals.get('price'):
            record = self.env['car.dekho.property'].browse(vals['car_id'])
            if record.offer_ids:
                maxOffer = max(record.mapped('offer_ids.price'))
                if maxOffer > vals['price']:
                    raise UserError('price not accepted')
            record.state = 'offer_received'
        return super().create(vals)               