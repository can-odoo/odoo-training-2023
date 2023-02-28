from odoo import fields, models, api

class TourGuide(models.Model):
    _name = 'tour.guide'
    _description = 'Tour Guide Things'

    name = fields.Char('Tour Name')
    description = fields.Char('Tour Description')
    # duration = fields.Integer('Duration(km)')
    # cost = fields.Float('cost',readonly=True)
    destination = fields.Char('Place Name')
    tour_type = fields.Selection(
        selection = [('group', 'Group'), ('solo', 'Solo'), ('family', 'Family')]
    )
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    active = fields.Boolean(string="Active",default=True)
    min_price = fields.Float("Min_Price", compute="_check_min_price")
    max_price = fields.Float("Max_Price", compute="_check_max_price")
    package_ids = fields.One2many('tour.packages','tour_ids')
    tag_ids = fields.Many2many('tour.tag')

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

                
