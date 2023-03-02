from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare

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
     garden_area = fields.Integer("Garden Area (sqm)")
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
     living_area = fields.Integer("Living Area (sqm)")
     garage = fields.Boolean()
     state = fields.Selection(string='Status',
                              selection=[('sold','Sold'),
                                         ('cancle','Cancle'),
                                         ('new','New'),
                                         ('offer received','Offer Received'),
                                         ('offer accepted','Offer Accepted')],
                              help="Type is used to seprate",
                              required=True,
                              copy=False,
                              default="new")
     user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
     buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
     tag_ids = fields.Many2many("estate.property.tag", string="Tags")
     #look up table create for manytomany
     offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")     
     total_area=fields.Integer(compute='_sum_total_area')
     best_price=fields.Float("Best Offer Price",compute='_best_price')

     _sql_constraints = [('ExpectedPrice','CHECK(expected_price > 0)', 'Expected price should be greater than 0'),
                         ('SellingPrice','CHECK(selling_price > 0)','Selling Price must be positive')]

     @api.depends('living_area','garden_area')
     def _sum_total_area(self):
          for i in self:
               i.total_area = i.garden_area + i.living_area
               
     @api.depends('offer_ids.price')
     def _best_price(self):
          for i in self:
               i.best_price = max(i.offer_ids.mapped('price')) if i.offer_ids else 0.0

     @api.onchange("garden")
     def _change_gardenArea_orien(self):
          if self.garden:
               self.garden_area=10
               self.garden_orientation='north'
          else:
               self.garden_area=0
               self.garden_orientation=False

     def set_sold(self):
          if self.state == "cancle": #"cancle" in self.mapped("state"):
               raise UserError("Cancled property not for sale")
          return self.write({"state":"sold"})
     
     def set_cancle(self):
          if "sold" in self.mapped("state"):
               raise UserError("sold property not be cancled")
          return self.write({"state":"cancle"})

     @api.constrains('selling_price','expected_price')
     def _check_sell_expec_90(self):
          for record in self: 
               if (float_compare(record.selling_price,record.expected_price * 90.0 / 100.0,precision_rounding=0.01)) < 0:
                    raise ValidationError('Selling price must be 90% of expected price')
               