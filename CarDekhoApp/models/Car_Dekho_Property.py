from odoo import fields, models

class CarDekhoProperty(models.Model):
     _name="car.dekho.property"
     _description="Car available at cheapest price"

     car_name = fields.Char(required=True)
     description = fields.Char()
     car_code=fields.Char()
     license_number=fields.Char(required=True)
     manufacturing_date= fields.Date()
     fuel_type=fields.Char()
     color = fields.Char(required=True)
     siting_capacity = fields.Integer(default='4')
     fuel_consumption = fields.Char()
     engine_frequency = fields.Selection(
          string='Type',
          selection=[('580hz', '580HZ'), 
                   ('660hz', '660HZ'), 
                   ('700hz', '700HZ'), 
                   ('above 700hz','Above 700HZ')],
          help="Type is used to separate")
     booking_date_upto=fields.Date()
     car_price = fields.Float()
     state = fields.Selection(string='Type',
                              selection=[('new','New'),
                                         ('old','Old'),
                                         ('modified', 'Modified')],
                              help="Type is used to seprate",
                              required=True,
                              copy=False,
                              default="new")


