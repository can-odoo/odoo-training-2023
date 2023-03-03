from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):
	_name='estate.property'
	_description = 'Real estate properties'
	_order = "id desc"

	name = fields.Char('Property Name', required=True)
	description = fields.Char('Description',required=True)
	postcode = fields.Char('PostCode', required=True)
	date_availability = fields.Date('Date Availability', default=fields.Date.add(fields.Date.today(),months=2) , copy=False)
	expected_price = fields.Float('Expected Price', required=True)
	selling_price = fields.Float('Selling Price', copy=False, readonly=True)
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

	# for find maximum best_price
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

	def action_to_status(self):
		for data in self:
			if data.state == 'sold':
				raise UserError("sold property can not be canceled")
			data.state = 'canceled'
		return True
	
	def action_to_sold(self):
		for data in self:
			if data.state == 'canceled':
				raise UserError("Canceled property can not be sold")
			data.state = 'sold'
		return True
	
	# sql constraints
	_sql_constraints = [
		('check_expected_price', 'CHECK(expected_price > 0)', 'The Expected price must be stricly Positive'),
		('check_selling_price', 'CHECK(selling_price >= 0)', 'The Selling Price must be strictly Positive'),
	]

	# @api.constrains('selling_price')
	# def check_selling_price(self):
	# 	for record in self:
	# 		value = record.expected_price*(0.9)
	# 		if record.selling_price and record.selling_price <= value:
	# 			raise ValidationError("Selling Price must be atleast 90% of Expected Price if you want to accept this offer")

	@api.constrains('selling_price', 'expected_price')
	def check_selling_price(self):
		for data in self:
			if not float_is_zero(data.selling_price, precision_digits = 2) and float_compare(data.selling_price, data.expected_price*(0.9), precision_digits = 2) == -1:
				raise ValidationError("Selling Price must be atleast 90% of Expected Price if you want to accept this offer")

