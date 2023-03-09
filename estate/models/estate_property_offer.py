from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Properties Offers'
    _order = "price"

    price = fields.Float('Price')
    status = fields.Selection(
        selection = [('accepted', 'Accepted'),('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)
    validity = fields.Integer('Validity(Days)', default=7)
    date_deadline = fields.Date('Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        # for data in self:
        #     if data.create_date:
        #         data.date_deadline = fields.Date.add(data.create_date.date(),days=data.validity)
        #     else:
        #         data.date_deadline = fields.Date.add(fields.Date.today(),days=data.validity)
        for data in self:
            date = data.create_date.date() if data.create_date else fields.Date.today()
            data.date_deadline = date + timedelta(days = data.validity)
    
    def _inverse_date_deadline(self):
        for data in self:
            # if data.create_date:
            #     data.validity = (data.date_deadline - data.create_date.date()).days
            # else:
            #     data.validity = (data.date_deadline - fields.Date.today()).days
            date = data.create_date.date() if data.create_date else fields.Date.today()
            data.validity = (data.date_deadline - date).days
    
    def to_action_accepted(self):
        for data in self:
            data.status = 'accepted'
            data.property_id.selling_price = data.price
            data.property_id.buyer_id = data.partner_id
            data.property_id.state = 'offer_accepted'
        return True
    
    def to_action_refused(self):
        for data in self:
            data.status = 'refused'
            data.property_id.selling_price = 0
        return True
    
    # sql constraints
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'The Offer Price must be Stricly Positive')
    ]

    @api.model
    def create(self,vals):
        x = self.env['estate.property'].browse(vals['property_id'])
        print("   ********     ", x)
        x.state = 'offer_received'
        if x.best_price > vals['price']:
            raise ValidationError(f'The Price should be greater than {x.best_price}')
        return super(EstatePropertyOffer, self).create(vals)