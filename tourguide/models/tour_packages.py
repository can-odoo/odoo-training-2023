from odoo import fields, models

class TourPackages(models.Model):
    _name = 'tour.packages'
    _description = 'Tour Packages'

    name = fields.Char('Name');
    duration = fields.Integer('Duration')
    price = fields.Float('Price')
    tour_ids = fields.Many2one('tour.guide', required=True)
    guide_id = fields.Many2one('res.users', string='TourGuide', default=lambda self: self.env.user)
    desc = fields.Text('Description')