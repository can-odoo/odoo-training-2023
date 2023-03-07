from odoo import models,fields,api

class franchiseProductOrder(models.Model):
    _name ="franchise.product.order"
    _description = "This is model contains order details"

    product_stock_id = fields.Many2one('franchise.product.stock',domain="[('status', '=', 'to_order')]", required=True)
    franchise_id =fields.Many2one(related="product_stock_id.franchise_id")
    quantity = fields.Integer(related ="product_stock_id.quantity")
    state = fields.Selection(selection=[('ordered','Ordered'),('shipped','Order Shipped'),('preparing','Preparing order'),('delivered', 'Delivered'),('canceled','Canceled')],required=True)
    price = fields.Float("Price",related ="product_stock_id.price" )
    payment = fields.Boolean()

    
    @api.onchange('state')
    def _onchange_state(self):
        for order in self:
            if order.state=="ordered":
                order.product_stock_id.status = order.state
            elif order.state=="delivered":
                order.product_stock_id.status = "in_stock"

    def canceled(self):
        for order in self:
            order.state="canceled"
    
    def delivered(self):
        for order in self:
            order.state="delivered"
