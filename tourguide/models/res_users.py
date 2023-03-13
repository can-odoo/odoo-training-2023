from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    tour_ids = fields.One2many('tour.guide','guide_id')
