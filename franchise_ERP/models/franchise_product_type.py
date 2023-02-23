from odoo import models,fields

class FranchiseProductType(models.Model):
    _name = "franchise.product.type"
    _description = "This is model stores the product type"

    name = fields.Char()