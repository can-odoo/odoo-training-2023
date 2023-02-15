from odoo import models, fields

class BuildProducts(models.Model):
    _name = "build.products"
    _description = "Build Products"

    name = fields.Char('Product Name' , required=True)
    description = fields.Char('Description', required=True)
    product_type = fields.Selection(selection=[('opc', 'OPC'), ('ppc', 'PPC')])
    product_grade = fields.Selection(selection=[('33', '33'), ('43', '43'), ('53', '53')])
    date_order = fields.Date('Date of Order')
    product_price = fields.Float('Product Price')
    product_quantity = fields.Integer('Product Quantity')
    total_price = fields.Float('Total Price')
    delivery_date = fields.Date('Expected Delivery Date')
