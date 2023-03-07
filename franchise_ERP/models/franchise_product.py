from odoo import models,fields

class FranchiseProduct(models.Model):
    _name = "franchise.product"
    _description = "This is Product model contains the information about product"
    _order = "name"

    name = fields.Char()
    price = fields.Float()
    description = fields.Char()
    categories = fields.Many2many('franchise.product.type')
    availability = fields.Boolean()
    