from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char('Property Name' , required=True)
    description = fields.Char('Description', required=True)
    postcode = fields.Char('Postcode' , required=True)
    date_availability = fields.Date('Date of Availability' , default=fields.Date.add(fields.Date.today(),months=3) , copy=False)
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price' , readonly=True , copy=False)
    bedrooms = fields.Integer('No. of Bedrooms' , default=2)
    property_type_id = fields.Many2one('estate.property.type' , string='Property Types')
    living_area = fields.Integer('Living Area (sqm)' , required=True)
    facades = fields.Integer('Facades' , required=True)
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden' )
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(selection=[('north', 'North'), ('south','South'), ('west','West'), ('east', 'East')])
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='State', default='new')
    active = fields.Boolean(string='Active' , default=True)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag' , string='Property Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    
