from odoo import models,fields

class ShowroomProperty(models.Model):
    _name = "showroom.property"
    _description = "This is showroom property module"

    name = fields.Char("Name of the firm")
    showroom_id = fields.Integer(required=True)
    address = fields.Text(required=True)
    showroom_owner = fields.Char(required=True)
    No_of_employee = fields.Integer("No of employee in each showroom")
    No_of_product = fields.Integer(default=0)
    Opening_date = fields.Date()
    total_sale = fields.Float("Total revanue generated :")
    date_of_stock_updated = fields.Date()
    showroom_start_time = fields.Date()
    showroom_close_time = fields.Date()
    parking_availabiliy = fields.Selection(selection=[('no','No'),('yes','Yes')])







