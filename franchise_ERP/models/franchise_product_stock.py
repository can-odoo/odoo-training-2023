from odoo import models,fields,api

class FranchiseProductStock(models.Model):
    _name = "franchise.product.stock"
    _description = "This model stores the details of stocks of perticular stores"

    name = fields.Char('Name',compute='_compute_name')
    product_id = fields.Many2one('franchise.product')
    franchise_id = fields.Many2one('franchise.store.property')
    quantity = fields.Integer()
    status = fields.Selection(selection=[('in_stock','In stock'),('out of stock','Out of Stock'),('to_order','To order'),('ordered', 'Ordered')])
    price = fields.Float("Price",compute="_compute_price",store=True)

    @api.onchange('quantity')
    def _onchange_quantity(self):
        for product in self:
            if product.quantity == 0:
                product.status = "out of stock"
            elif product.quantity>0 :
                product.status = "in_stock"
            else:
                product.status="to_order"

    @api.depends('quantity','product_id')
    def _compute_price(self):
        for product in self:                                     
            product.price = (product.product_id.price * product.quantity)

    @api.depends('product_id')
    def _compute_name(self):
        for record in self:
            record.name = record.franchise_id.name + " - " + record.product_id.name

    def action_order(self):
        for product in self:
            product.status = "ordered"
