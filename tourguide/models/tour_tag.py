from odoo import models, fields

class TourTag(models.Model):
    _name = 'tour.tag'
    _description = 'Tour Tags'

    name = fields.Char('Tour Tags', required=True)
    color = fields.Integer('Color')