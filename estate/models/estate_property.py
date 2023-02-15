from odoo import models, fields

class EstateProperty(models.Model):
	_name='estate.property'
	_description = 'Real estate properties'

	name = fields.Char('Property Name', required=True)
	description = fields.Char('Description',required=True)
	postcode = fields.Char('PostCode', required=True)
	date_availability = fields.Date('Date Availability')
	expected_price = fields.Float('Expected Price', required=True)
	selling_price = fields.Float('Selling Price')
	bedrooms = fields.Integer('BedRooms')
	living_area = fields.Integer('Living Area')
	facades = fields.Integer('Facades')
	garage = fields.Boolean('Garage')
	garden = fields.Boolean('Garden')
	garden_area = fields.Integer('Garden Area')
	garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        )

