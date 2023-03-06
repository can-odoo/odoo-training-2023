from odoo import fields, models

class carTags(models.Model):
    _name="cardekho.property.tag"
    _description="Car Tag Here"
    _order="name"

    name = fields.Char('Car Tag',required=True)
    color = fields.Integer('Color')
    _sql_constraints = [('Tagname','UNIQUE(name)','Property tag name must be unique')]