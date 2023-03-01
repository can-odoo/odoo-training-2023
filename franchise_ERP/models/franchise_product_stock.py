from odoo import models,fields,api

class FranchiseProductStock(models.Model):
    _name = "franchise.product.stock"
    _description = "This model stores the details of stocks of perticular stores"

    product_id = fields.Many2one('franchise.product')
    franchise_id = fields.Many2one('franchise.store.property')
    quantity = fields.Integer()
    status = fields.Selection(selection=[('in_stock','In stock'),('out of stock','Out of Stock'),('ordered', 'Ordered')])
    price = fields.Integer("Price",compute="_compute_price")

    @api.onchange('quantity')
    def _onchange_quantity(self):
        for product in self:
            if product.quantity == 0:
                product.status = "out of stock"
            elif product.quantity>0 :
                product.status = "in_stock"

    @api.depends('quantity','product_id','status')
    def _compute_price(self):
        for product in self:
            product.price = (product.product_id.price * product.quantity)
            if product.status=='ordered':
                product.price = (-1)*product.price