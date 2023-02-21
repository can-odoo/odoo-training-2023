from odoo import models,fields

class FranchiseProperty(models.Model):
    _name = "franchise.property"
    _description = "This is showroom property module"

    name = fields.Char("Firm")
    franchise_id = fields.Integer(required=True)
    franchise_owner = fields.Char(required=True)
    no_of_product = fields.Integer(default=0)
    location = fields.Char()
    opening_date = fields.Date(default = fields.Date.today)
    total_sale = fields.Float(copy=False)
    total_revanue = fields.Float("Total revanue :",readonly=True,default=True,copy=False) 
    phone_no =fields.Char(size=10)
    type_franchise = fields.Selection(selection = [('job franchise','job franchise'),('product franchise','product franchise'),('business format franchise','business format franchise'),('investment franchise','investment franchise'),('conversion franchise','conversion franchise')])
    active = fields.Boolean(active=True)




