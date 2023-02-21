from odoo import models,fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Test Model"

    name = fields.Char('Title',required=True)
    description = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date('Available from',copy=False,default= fields.Date.add(fields.date.today(),months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, default='0.0',copy=False) 
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer('Living Area ( sqm )')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[('north','North'),('east','East'),('west','West'),('south','South')])
    active = fields.Boolean( default=True,active=True)
    state = fields.Selection(selection =[('new','New'), ('Offer_Received','Offer Received'), ('Offer_Accepted','Offer Accepted'), ('Sold_Canceled','Sold Canceled')], default='new')


    
