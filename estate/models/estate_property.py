from odoo import api,models,fields,exceptions
from odoo.tools.float_utils import float_compare,float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Test Model"

    name = fields.Char('Title',required=True)
    description = fields.Char()
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type")
    tag_ids = fields.Many2many('estate.property.tag',string="Tags")
    postcode = fields.Char(required=True)
    date_availability = fields.Date('Available from',copy=False,default= fields.Date.add(fields.date.today(),months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, default='0.0',copy=False) 
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer('Living Area ( sqm )')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[('north','North'),('east','East'),('west','West'),('south','South')])
    active = fields.Boolean( default=True,active=True)
    state = fields.Selection(selection =[('new','New'), ('offer_received','Offer Received'), ('offer_accepted','Offer Accepted'), ('sold_canceled','Sold Canceled')], default='new')
    salesman = fields.Many2one('res.users',string="Salesman", default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner',copy =False)
    offer_ids = fields.One2many('estate.property.offer','property_id')
    total_area = fields.Float('Total area ( sqm )',compute="_compute_total")
    best_offer = fields.Float("Best offer",compute="_compute_bestoffer")


    @api.depends('garden_area','living_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.garden_area+record.living_area

    @api.depends('offer_ids')
    def _compute_bestoffer(self):
        for record in self: 
            if record.offer_ids:    
                self.best_offer = max(record.offer_ids.mapped('price'))
            else:
                self.best_offer = 0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_orientation="north"
            self.garden_area = 10
        else:
            self.garden_area = 0
            self.garden_orientation=None

    def action_sold(self):
        for record in self:
            if record.state=="sold_canceled":
                raise exceptions.UserError("A canceled property cannot be sold")
            record.state = "offer_accepted"
        return True

    def action_cancel(self):
        for record in self:
            if record.state=="offer_accepted":
                raise exceptions.UserError("A sold property cannot be canceled.")
            record.state = "sold_canceled" 
        return True
    
    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for record in self:
            if not float_is_zero(record.selling_price,0) and float_compare(record.selling_price,record.expected_price*(0.9),2)==-1:
                raise exceptions.ValidationError("the selling price cannot be lower than 90% of the expected price.")

    _sql_constraints = [
        ('check_expected_price_1', 'CHECK(expected_price > 0)', 'A property expected price must be strictly positive'),
        ('check_selling_price_1', 'CHECK(selling_price >= 0)', 'A property selling price must be positive'),
    ]