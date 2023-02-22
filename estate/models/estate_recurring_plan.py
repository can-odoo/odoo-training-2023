from odoo import fields, models

class RecurringPlan(models.Model):
     _name="estate.recurring.plan"
     _description="Estate Property revenue plans"

     name = fields.Char('Property Name',required=True)
     description = fields.Char()
     # many2one mapping
     property_type_id = fields.Many2one("estate.property.type", string="Property Type")
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
     user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
     buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
     tag_ids = fields.Many2many("estate.property.tag", string="Tags")
     offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")