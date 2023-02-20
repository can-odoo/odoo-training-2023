from odoo import fields, models

class TourGuide(models.Model):
    _name = 'tour.guide'
    _description = 'Tour Guide Things'

    name = fields.Char('Tour Name')
    description = fields.Char('Tour Description')
    duration = fields.Integer('Duration')
    cost = fields.Float('cost',readonly=True)
    destination = fields.Char('Place Name')
    tour_type = fields.Selection(
        selection = [('group', 'Group'), ('solo', 'Solo'), ('family', 'Family')]
    )
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    