from odoo import fields, models

class RecurringPlan(models.Model):
     _name="estate.recurring.plan"
     _description="Estate Property revenue plans"

     name = fields.Char(required=True)
     description = fields.Char()
     postalcode = fields.Char()
     date_availability = fields.Date()
     expected_price = fields.Float(required=True)
     selling_price = fields.Float()
     bedrooms = fields.Integer()
     living_area = fields.Integer()
     garden = fields.Boolean()
     garden_orientation = fields.Selection(
        string='Type',
        selection=[('east', 'East'), 
                   ('west', 'West'), 
                   ('north','North'), 
                   ('south','South')],
        help="Type is used to separate")
