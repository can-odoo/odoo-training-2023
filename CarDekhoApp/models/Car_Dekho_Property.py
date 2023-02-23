from odoo import fields, models

class CarDekhoProperty(models.Model):
     _name="car.dekho.property"
     _description="Car available at cheapest price"
     
     _rec_name="car_name"
     car_name = fields.Char('Name',required=True)
     description = fields.Char()
     car_code=fields.Char()
     license_number=fields.Char(required=True)
     manufacturing_date= fields.Date()
     fuel_type=fields.Char()
     color = fields.Char(required=True)
     siting_capacity = fields.Integer(default='4')
     fuel_consumption = fields.Char()
     engine_frequency = fields.Selection(
          string='Engine Frequency',
          selection=[('580hz', '580HZ'), 
                   ('660hz', '660HZ'), 
                   ('700hz', '700HZ'), 
                   ('above 700hz','Above 700HZ')],
          help="Type is used to separate")
     booking_date_upto=fields.Date()
     car_price = fields.Float()
     state = fields.Selection(string='State',
                              selection=[('new','New'),
                                         ('old','Old'),
                                         ('modified', 'Modified')],
                              help="Type is used to seprate",
                              required=True,
                              copy=False,
                              default="new")
     car_property_id = fields.Many2one("cardekho.property.type",string="Car Type")
     user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
     buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
     tag_ids = fields.Many2many("cardekho.property.tag", string="Tags")
     offer_ids = fields.One2many("cardekho.property.offer", "car_id", string="Offers")