from odoo import fields, models

class PropertyTags(models.Model):
    _name="estate.property.tag"
    _description="Estate Property Tag"

    name = fields.Char('Property Tag',required=True)


