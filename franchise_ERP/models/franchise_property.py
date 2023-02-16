from odoo import models,fields

class FranchiseProperty(models.Model):
    _name = "franchise.property"
    _description = "This is showroom property module"

    name = fields.Char("Name of the firm")
    franchise_id = fields.Integer(required=True)
    franchise_owner = fields.Char(required=True)
    no_of_product = fields.Integer(default=0)
    opening_date = fields.Date()
    total_sale = fields.Float()
    total_revanue = fields.Float("Total revanue generated :") 
    phone_no =fields.Char()
    type_franchise = fields.Char()






