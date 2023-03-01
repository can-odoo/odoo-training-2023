from odoo import api,models,fields

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
    state = fields.Selection(selection =[('new','New'), ('Offer_Received','Offer Received'), ('Offer_Accepted','Offer Accepted'), ('Sold_Canceled','Sold Canceled')], default='new')
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
