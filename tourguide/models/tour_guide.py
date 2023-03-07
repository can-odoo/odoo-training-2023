from odoo import fields, models, api
from datetime import datetime, timedelta

class TourGuide(models.Model):
    _name = 'tour.guide'
    _description = 'Tour Guide Things'

    name = fields.Char('Tour Name')
    description = fields.Char('Tour Description')
    price = fields.Float('Price')
    destination = fields.Char('Place Name')
    duration = fields.Integer('Duration',default = 6, compute="_compute_duration", inverse="_set_duration", store=True)
    desc = fields.Text("Desc")
    tour_type = fields.Selection(
        selection = [('group', 'Group'), ('solo', 'Solo'), ('family', 'Family')]
    )
    status = fields.Selection(
        selection = [('available', 'Available'), ('unavailable', 'Unavailable')], 
    )
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    tag_ids = fields.Many2many('tour.tag')
    guide_id = fields.Many2one('res.users', string="TourGuide", default=lambda self:self.env.user)

    @api.depends('package_ids.price')
    def _check_min_price(self):
        for l in self:
            if self.package_ids:
                self.min_price = min(self.package_ids.mapped('price'))
            else:
                self.min_price = 0
    
    def _check_max_price(self):
        for l in self:
            if self.package_ids:
                self.max_price = max(self.package_ids.mapped('price'))
            else:
                self.max_price = 0

    @api.depends('start_date','end_date')
    def _compute_duration(self):
        for data in self:
            if data.start_date and data.end_date:
                data.duration = (data.end_date - data.start_date).days
    
    def _set_duration(self):
        for data in self:
            if data.start_date and data.duration:
                data.end_date = data.start_date + timedelta(days = data.duration)
    
    #sql constraints
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'Tour Price must be Stricly Positive'),
        ('check_duration', 'CHECK(duration > 0)', 'Duration should be positive')
    ]