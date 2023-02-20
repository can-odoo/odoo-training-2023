from odoo import models, fields

class BuildProducts(models.Model):
    _name = "build.products"
    _description = "Build Products"
     

    name = fields.Char('Product Name' , required=True)
    description = fields.Char('Description', required=True)
    product_type = fields.Selection(selection=[('opc', 'OPC'), ('ppc', 'PPC')])
    product_grade = fields.Selection(selection=[('33', '33'), ('43', '43'), ('53', '53')])
    product_price = fields.Float('Product Price')
    product_quantity = fields.Integer('Product Quantity')
    total_price = fields.Float('Total Price')
    date_order = fields.Date('Date of Order')
    delivery_date = fields.Date('Expected Delivery Date' , default=fields.Date.add(fields.Date.today(), days=2))
    state = fields.Selection([
        ('new', 'New'),
        ('oder_accepted', 'Order Accepted'),
        ('in_progress', 'In Progress'),
        ('in_delivery', 'In Delivery'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    ], string='State', default='new')
    active = fields.Boolean(string='Active', default=True)
