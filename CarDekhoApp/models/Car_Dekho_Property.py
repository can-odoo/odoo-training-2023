from odoo import fields, models

class CarDekhoProperty(models.Model):
     _name="car.dekho.property"
     _description="Car available at cheapest price"

     name = fields.Char()
     description = fields.Char()
     price = fields.Float()
     color = fields.Char()
     siting_capacity = fields.Integer()
     fuel_consumption = fields.Char()
     engine_frequency = fields.Char()
     modified_date = fields.Date()
     
     
     
     
