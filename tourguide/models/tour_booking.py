from odoo import fields, models, api
from odoo.exceptions import ValidationError

class TourBooking(models.Model):
    _name = 'tour.booking'
    _description = 'Tour Bookings'

    name = fields.Char('Customer Name', required=True)
    booking_date = fields.Date('Booking Date', default=fields.Date.today(), required=True)
    booking_status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], string='Booking Status', default='draft', required=True)
    total_cost = fields.Float('Total Cost', compute="_total_cost", store=True)
    # tour_name = fields.Char('Tour',store=True)
    tour_guide_id = fields.Many2one('tour.guide', string='Tour', store=True)
    guide = fields.Char('Tour Guide')
    ticket_qty = fields.Integer(string='Ticket for Multiple Persons', default=1)


    @api.onchange('tour_guide_id')
    def onchange_tour_guide_id(self):
        if self.tour_guide_id:
            # self.tour_name = self.tour_guide_id.name
            self.guide = self.tour_guide_id.guide_id.name
    
    @api.depends('tour_guide_id','ticket_qty')
    def _total_cost(self):
        for data in self:
            data.total_cost = data.tour_guide_id.price * data.ticket_qty

    @api.constrains('booking_date', 'tour_guide_id', 'booking_status')
    def check_booking_date(self):
        for booking in self:
            if booking.booking_date < fields.Date.today():
                raise ValidationError("Booking date cannot be in the past.")
            if booking.booking_status == 'draft' and booking.tour_guide_id and booking.booking_date > booking.tour_guide_id.start_date:
                raise ValidationError("Booking date cannot be after tour start date.")
            if booking.booking_status == 'confirmed' and booking.tour_guide_id and booking.booking_date > booking.tour_guide_id.end_date:
                raise ValidationError("Booking date cannot be after tour end date.")