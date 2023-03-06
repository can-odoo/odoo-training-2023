from odoo import models,fields

class FranchiseProductType(models.Model):
    _name = "franchise.product.type"
    _description = "This is model stores the product type"

    name = fields.Char()
    color = fields.Integer()


    _sql_constraints = [ ('check_product_type','UNIQUE (name)','Product Type should be unique')]