from odoo import models, fields
from odoo import api

class BuildProductsOrder(models.Model):
    _name = 'build.products.order'
    _description = 'Build Products Order'
    
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    order_date = fields.Date(string='Order Date', default=fields.Date.today())
    qty_ordered = fields.Float(string='Quantity Ordered', required=True)
    delivery_address = fields.Text(string='Delivery Address', required=True)
    delivery_date = fields.Date('Expected Delivery Date' , default=fields.Date.add(fields.Date.today(), days=2))
    state = fields.Selection([
        ('new', 'New'),
        ('oder_accepted', 'Order Accepted'),
        ('in_progress', 'In Progress'),
        ('in_delivery', 'In Delivery'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    ], string='State', default='new')
    status = fields.Selection([
        ('accepted' , 'Accepted'),
        ('refused' , 'Refused')
    ], string='Status', required=True)
    product_id = fields.Many2one('build.products', string='Product', required=True)
    total_amount = fields.Float(compute='_compute_total_amount' , inverse='_inverse_total_amount' , string='Total Amount' , store=True)

    @api.depends('qty_ordered', 'product_id.product_price')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = order.qty_ordered * order.product_id.product_price

    def _inverse_total_amount(self):
        for order in self:
            order.qty_ordered = order.total_amount / order.product_id.product_price

    

    