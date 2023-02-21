from odoo import fields, models

class RecurringPlan(models.Model):
     _name="estate.recurring.plan"
     _description="Estate Property revenue plans"

     name = fields.Char('Property Name',required=True)
     description = fields.Char()
     property_type_id = fields.Char()
     postalcode = fields.Char()
     expected_price = fields.Float(required=True)
     bedrooms = fields.Integer(default='2')
     facades = fields.Integer()
     garden = fields.Boolean()
     active=fields.Boolean(active=False, default=True)
     garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('east', 'East'), 
                   ('west', 'West'), 
                   ('north','North'), 
                   ('south','South')],
        help="Type is used to separate")
     date_availability = fields.Date(copy=False, default=fields.Date.add(fields.Date.today(),months=3))
     selling_price = fields.Float(readonly='1', copy=False)  #for read only field readonly=1 
     living_area = fields.Integer()
     garage = fields.Boolean()
     state = fields.Selection(string='State',
                              selection=[('new','New'),
                                         ('offer received','Offer Received'),
                                         ('offer accepted', 'Offer Accepted'),
                                         ('sold and canceled','Sold And Canceled')],
                              help="Type is used to seprate",
                              required=True,
                              copy=False,
                              default="new")