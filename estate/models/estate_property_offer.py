from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'

    price = fields.Float('Price')
    status = fields.Selection([
        ('accepted' , 'Accepted'),
        ('refused' , 'Refused')
    ], string='Status', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', strin='Property', required=True)

