from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char('Property Name' , required=True)
    description = fields.Char('Description', required=True)
    postcode = fields.Char('Postcode' , required=True)
    date_availability = fields.Date('Date of Availability')
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('No. of Bedrooms' , required=True)
    living_area = fields.Integer('Living Area (sqm)' , required=True)
    facades = fields.Integer('Facades' , required=True)
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden' )
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(selection=[('north', 'North'), ('south','South'), ('west','West'), ('east', 'East')])
