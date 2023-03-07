from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class propertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _order = "price desc"

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
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.recurring.plan", string="Property", required=True)
    validity = fields.Integer("Validity",default=7)
    date_deadline = fields.Date("Deadline", compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    property_type_id = fields.Many2one(related='property_id.property_type_id',store=True,string='Property Type')

    _sql_constraints = [('OfferPrice','CHECK(price > 0)','Offer price must be positive')]

    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for i in self:
            date = i.create_date.date() if i.create_date else fields.Date.today()
            i.date_deadline = date + relativedelta(days=i.validity)

    def _inverse_date_deadline(self):
        for i in self:
            date = i.create_date.date() if i.create_date else fields.Date.today()
            i.validity = (i.date_deadline - date).days

    def accept_state(self):
        self.write({'state':'accepted'})
        return self.mapped("property_id").write({'state':'offer_accepted',
                                                 'buyer_id':self.partner_id.id,
                                                 'selling_price':self.price
                                                })
    def refused_state(self):
        self.write({'state':'refused'})

    @api.model
    def create(self,vals):
        if vals.get('property_id') and vals.get('price'):
            record = self.env['estate.recurring.plan'].browse(vals['property_id'])
            if record.offer_ids:
                maxOffer = max(record.mapped('offer_ids.price'))
                if maxOffer > vals['price']:
                    raise UserError('price not accepted')
            record.state = 'offer_received'
        return super().create(vals)            
