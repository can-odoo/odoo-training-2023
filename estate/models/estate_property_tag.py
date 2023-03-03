from odoo import fields, models

class PropertyTags(models.Model):
    _name="estate.property.tag"
    _description="Estate Property Tag"
    _order="name"

    name = fields.Char('Property Tag',required=True)
    color = fields.Integer('Color')
    _sql_constraints = [('Tagname','UNIQUE(name)','Property tag name must be unique')]