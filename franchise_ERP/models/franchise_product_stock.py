from odoo import models,fields

class FranchiseProductStock(models.Model):
    _name = "franchise.product.stock"
    _description = "This model stores the details of stocks of perticular stores"

    product_id = fields.Many2one('franchise.product')
    franchise_id = fields.Many2one('franchise.store.property')
    quantity = fields.Integer()
    status = fields.Selection(selection=[('In stock','in_stock'),('out of stock','Out of Stock'),('ordered', 'Ordered')])
