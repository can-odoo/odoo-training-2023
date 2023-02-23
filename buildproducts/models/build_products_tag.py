from odoo import models, fields

class BuildProductsTag(models.Model):
    _name = 'build.products.tag'
    _description = 'Build Products Tag'

    name = fields.Char('Products Tags', required=True)