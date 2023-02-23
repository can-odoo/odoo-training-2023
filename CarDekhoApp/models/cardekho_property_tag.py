from odoo import fields, models

class carTags(models.Model):
    _name="cardekho.property.tag"
    _description="Car Tag Here"

    name = fields.Char('Car Tag',required=True)