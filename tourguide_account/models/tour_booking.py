from odoo import fields, models

class TourBooking(models.Model):
    _inherit='tour.booking'

    def action_to_confirm(self):
        print("invoice generate1212121")
        return super(TourBooking, self).action_to_confirm()