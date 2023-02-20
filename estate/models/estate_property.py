from odoo import models, fields

class EstateProperty(models.Model):
	_name='estate.property'
	_description = 'Real estate properties'

	name = fields.Char('Property Name', required=True)
	description = fields.Char('Description',required=True)
	postcode = fields.Char('PostCode', required=True)
	date_availability = fields.Date('Date Availability', default=fields.Date.add(fields.Date.today(),months=3) , copy=False)
	expected_price = fields.Float('Expected Price', required=True)
	selling_price = fields.Float('Selling Price', readonly=True, copy=False)
	bedrooms = fields.Integer('BedRooms', default=2)
	living_area = fields.Integer('Living Area')
	facades = fields.Integer('Facades')
	garage = fields.Boolean('Garage')
	garden = fields.Boolean('Garden')
	garden_area = fields.Integer('Garden Area')
	garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        )
	active = fields.Boolean(string="Active",default=True)
	state = fields.Selection(
		selection=[('new', 'New'), 
	     ('offer_received', 'Offer Received'), 
		 ('offer_accepted', 'Offer Accepted'), 
		 ('sold', 'Sold'),
		 ('canceled', 'Canceled')],
		 default='new', required=True, copy=False
	)

