from odoo import models, fields, api

class EstateProperty(models.Model):
	_name='estate.property'
	_description = 'Real estate properties'

	name = fields.Char('Property Name', required=True)
	description = fields.Char('Description',required=True)
	postcode = fields.Char('PostCode', required=True)
	date_availability = fields.Date('Date Availability', default=fields.Date.add(fields.Date.today(),months=2) , copy=False)
	expected_price = fields.Float('Expected Price', required=True)
	selling_price = fields.Float('Selling Price', readonly=True, copy=False)
	bedrooms = fields.Integer('No of BedRooms', default=2)
	living_area = fields.Integer('Living Area(sqm)')
	facades = fields.Integer('Facades')
	garage = fields.Boolean('Garage')
	garden = fields.Boolean('Garden')
	garden_area = fields.Integer('Garden Area')
	total_area = fields.Integer('Total Area(sqm)',compute="_sum_total")
	best_price = fields.Float('Best Offer', compute="_check_best_price")
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
	property_type_id = fields.Many2one('estate.property.type')
	user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
	buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
	tax_ids = fields.Many2many('estate.property.tag') 
	offer_ids = fields.One2many('estate.property.offer', 'property_id')
	
	# for sum of two values
	@api.depends("living_area", "garden_area")
	def _sum_total(self):
		for data in self:
			data.total_area = data.living_area + data.garden_area

	# @api.depends("offer_ids.price")
	# def _check_best_price(self):
	# 	for data in self:
	# 		best_price = 0
	# 		for l in data.offer_ids:
	# 			if l.price > best_price:
	# 				best_price = l.price
	# 		data.best_price = best_price

	@api.depends("offer_ids.price")
	def _check_best_price(self):
		for data in self:
			if data.offer_ids:
				data.best_price = max(data.offer_ids.mapped('price'))
			else:
				data.best_price = 0
	

	@api.onchange("garden")
	def _onchange_garden(self):
		if self.garden:
			self.garden_area = 10
			self.garden_orientation = 'north'
		else:
			self.garden_area = 0
			self.garden_orientation = False

