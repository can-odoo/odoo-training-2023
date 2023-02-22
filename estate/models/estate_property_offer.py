from odoo import models,fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is offer model contains the offers rais for perticular properties"

    price = fields.Float()
    status = fields.Selection(selection =[('accepted','Accepted'),('refused','Refused')], copy=False)
    partner_id = fields.Many2one('res.partner',required = True)
    property_id = fields.Many2one('estate.property', required=True)