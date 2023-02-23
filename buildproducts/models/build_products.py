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
    active = fields.Boolean(string='Active', default=True)
    order_ids = fields.One2many('build.products.order', 'product_id', string='Orders')
    tag_ids = fields.Many2many('build.products.tag' , string='Product Tags')
