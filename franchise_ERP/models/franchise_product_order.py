from odoo import models,fields

class franchiseProductOrder(models.Model):
    _name ="franchise.product.order"
    _description = "This is model contains order details"

    product_id = fields.Many2one('franchise.product')
    franchise_id = fields.Many2one('franchise.store.property')
    quantity = fields.Integer()
    status = fields.Selection(selection=[('ordered','Ordered'),('shipped','Order Shipped'),('preparing','Preparing order'),('delivered', 'Delivered')])
    price = fields.Float("Price",compute="_compute_price")
    payment = fields.Boolean()

