from odoo import models,fields

class FranchiseStoreProperty(models.Model):
    _name = "franchise.store.property"
    _description = "This is showroom property module"

    # franchise_id = fields.Integer(required=True)
    name = fields.Char("Firm")
    franchise_owner = fields.Char()
    store_manager = fields.Many2one('res.users',required =True)
    no_of_product = fields.Integer(default=0)
    location = fields.Char()
    opening_date = fields.Date(default = fields.Date.today)
    sale = fields.Float(copy=False)
    revanue = fields.Float("Total revanue :",readonly=True,default=True,copy=False) 
    phone_no =fields.Char(size=10)
    no_of_employee = fields.Integer()
    # type_franchise = fields.Selection(selection = [('job franchise','job franchise'),('product franchise','product franchise'),('business format franchise','business format franchise'),('investment franchise','investment franchise'),('conversion franchise','conversion franchise')])
    available = fields.Boolean("Active")
    product_ids = fields.One2many('franchise.product.stock','franchise_id')




