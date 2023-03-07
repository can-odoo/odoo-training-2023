from odoo import models,fields,api

class FranchiseStoreProperty(models.Model):
    _name = "franchise.store.property"
    _description = "This is showroom property module"
    _order = "sequence"

    # franchise_id = fields.Integer(required=True)
    name = fields.Char("Firm",required=True)
    franchise_owner = fields.Char()
    store_manager = fields.Many2one('res.users',required =True)
    no_of_product = fields.Integer(default=0)
    location = fields.Char()
    opening_date = fields.Date(default = fields.Date.today)
    sale = fields.Float("Net sale ", copy=False)
    profit_margin = fields.Float("Profit Margin ( % )")
    net_revanue = fields.Float("Total revanue ( rs ) :",default=0,compute="_compute_revanue",inverse="_inverse_revanue") 
    phone_no =fields.Char(size=10)
    no_of_employee = fields.Integer()
    # type_franchise = fields.Selection(selection = [('job franchise','job franchise'),('product franchise','product franchise'),('business format franchise','business format franchise'),('investment franchise','investment franchise'),('conversion franchise','conversion franchise')])
    available = fields.Boolean("Active",default=True)
    product_ids = fields.One2many('franchise.product.stock','franchise_id')
    order_ids = fields.One2many('franchise.product.order','franchise_id')
    sequence = fields.Integer()


    @api.depends('sale','profit_margin')
    def _compute_revanue(self):
        for store in self:
            store.net_revanue = store.sale * store.profit_margin/100

    def _inverse_revanue(self):
        for store in self:
            if store.sale:
                store.profit_margin = store.net_revanue*100/store.sale

    @api.onchange('available')
    def _onchange_available(self):
        for store in self:
            if store.available==False:
                return {'warning': {
                'title': ("Warning"),
                'message': ('Store closed !!')}}            

    def action_open(self):
        for store in self:
            store.available = True

    def action_close(self):
        for store in self:
            store.available = False
        

    _sql_constraints = [
        ('check_sale','CHECK(sale >= 0)','A sale must be positive'),
        ('check_net_revanue','CHECK(price >= 0)','A net_revanue  must be positive'),
        ('check_profit_margin','CHECK(profit_margin >= 0 AND profit_margin<=100)','A profit margin must be under 100.'),
    ]