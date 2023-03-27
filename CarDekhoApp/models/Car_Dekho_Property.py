from odoo import fields, models,api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare,float_is_zero

class CarDekhoProperty(models.Model):
     _name="car.dekho.property"
     _description="Car available at cheapest price"
     _order="id desc"
     
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
     state = fields.Selection(string='Status',
                              selection=[('new','New'),
                                         ('sold','Sold'),
                                         ('cancel','Cancel'),
                                         ('modified','Modified'),
                                         ('offer_received','Offer received'),
                                         ('offer_accepted','Offer Accepted')],
                              required=True,
                              copy=False,
                              default="new")
     car_property_id = fields.Many2one("cardekho.property.type",string="Car Type")
     user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
     buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
     tag_ids = fields.Many2many("cardekho.property.tag", string="Tags")
     offer_ids = fields.One2many("cardekho.property.offer", "car_id", string="Offers")
     best_price = fields.Float("Best Offer", compute='_best_price_offer')
     height = fields.Float("Height (M)")
     width = fields.Float("Width (W)")
     t_area = fields.Float("Area (Sqm)", compute='_total_area')
     weight=fields.Integer("Weight (KG)", compute='_approx_weight')
     selling_price = fields.Float(readonly='1', copy=False)

     _sql_constraints = [('CarPrice','CHECK(car_price > 0)', 'Car price should be greater than 0'),
                         ('SellingPrice','CHECK(selling_price > 0)','Selling Price must be positive'),
                         ('LicenseNumber','UNIQUE(license_number)','License Number should be unique')]
     
     @api.depends('offer_ids.price')
     def _best_price_offer(self):
          for offer in self:
               offer.best_price = max(offer.offer_ids.mapped('price')) if offer.offer_ids else 0.0                    

     @api.depends('height','width')
     def _total_area(self):
          for i in self:
               i.t_area = i.height * i.width                         

     @api.onchange('t_area')
     def _change_state_area(self):
          if self.t_area > 40.00:
               self.state='modified'
          else : 
               self.state='new'

     @api.onchange('siting_capacity')
     def _change_engine_freq(self):
          if self.siting_capacity >=6:
               self.engine_frequency = 'above 700hz'
          else:
               self.engine_frequency = False
     @api.depends('siting_capacity')
     def _approx_weight(self):
          if self.siting_capacity > 5:
               self.weight = 100
          else :
               self.weight=0

     def car_sold(self):
          if self.state == 'cancel':
               raise UserError("Cancled car not for sale")
          return self.write({'state':'sold'})

     def car_cancle(self):
          if self.state == 'sold':
               raise UserError("sold car not be cancel")
          return self.write({'state':'cancel'})

     @api.constrains('selling_price','car_price')
     def _check_sell_expec_80(self):
          for record in self: 
               if (not float_is_zero(record.selling_price, precision_rounding=0.01)
                   and float_compare(record.selling_price,record.car_price * 80.0 / 100.0,precision_rounding=0.01)) < 0:
                   raise ValidationError('Selling price must be 80% of car price')               

     #Python inheritance
     def unlink(self):
          if not set(self.mapped('state'))=={'new','cancel'}:
               raise UserError('Not be possible to delete')
          return super.unlink()          