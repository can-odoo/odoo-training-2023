from odoo import models, fields
from odoo import api

class BuildProducts(models.Model):
    _name = "build.products"
    _description = "Build Products"
     
    name = fields.Char('Product Name' , required=True)
    description = fields.Char('Description', required=True)
    product_type = fields.Selection(selection=[('opc', 'OPC'), ('ppc', 'PPC')])
    product_grade = fields.Selection(selection=[('33', '33'), ('43', '43'), ('53', '53')])
    product_price = fields.Float('Product Price')
    product_quantity = fields.Integer('Product Quantity')
    active = fields.Boolean(string='Active', default=True)
    order_ids = fields.One2many('build.products.order', 'product_id', string='Orders')
    tag_ids = fields.Many2many('build.products.tag' , string='Product Tags')
    total_sale = fields.Float(string='Total Sales' , compute='_compute_total_sales')

    @api.onchange('order_ids')
    def _onchange_order_qty(self):
        for product in self:
            ordered_qty = sum(order.qty_ordered for order in product.order_ids)
            if ordered_qty:
                product.product_quantity = product._origin.product_quantity - ordered_qty

    @api.depends('order_ids')
    def _compute_total_sales(self):
        for record in self:
            if record.order_ids:
                record.total_sale = sum(record.order_ids.mapped('total_amount'))
            else:
                record.total_sale=0.0