from odoo import models, fields, api
from datetime import datetime, timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Properties Offers'

    price = fields.Float('Price')
    status = fields.Selection(
        selection = [('accepted', 'Accepted'),('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
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
            



