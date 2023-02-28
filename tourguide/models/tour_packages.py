from odoo import fields, models, api
from datetime import datetime, timedelta

class TourPackages(models.Model):
    _name = 'tour.packages'
    _description = 'Tour Packages'

    name = fields.Char('Name');
    price = fields.Float('Price')
    tour_start = fields.Date('Tour_Start', )
    tour_end = fields.Date('Tour_End',compute="_change_tour_end", inverse="_total_days")
    duration = fields.Integer('Duration',default = 7)
    tour_ids = fields.Many2one('tour.guide', required=True)
    guide_id = fields.Many2one('res.users', string='TourGuide', default=lambda self: self.env.user)
    desc = fields.Text('Description')

    @api.depends('tour_start', 'tour_end')
    def _total_days(self):
        for data in self:
            if data.tour_start and data.tour_end:
                duration = (data.tour_end - data.tour_start).days 
                data.duration = duration

    @api.depends('duration', 'tour_start')
    def _change_tour_end(self):
        for data in self:
            if data.tour_start and data.duration:
                data.tour_end = data.tour_start + timedelta(days=data.duration)
