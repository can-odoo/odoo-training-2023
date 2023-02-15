from odoo import models, fields

class WasteManagement(models.Model):
    _name = 'waste.management'
    _description = 'Waste Management'

    name = fields.Char('Waste Product Name', required=True)
    description = fields.Char('Description',required=True)
    product_type = fields.Selection(
        selection = [('paper','Paper'), ('glass','Glass'), ('plastic','Plastic'), ('organic','Organic')])
    quantity = fields.Float('Quantity')
    disposal_date = fields.Date('Disposal Date')
    disposal_vendor = fields.Char('Disposal Vendor')
    collection_date = fields.Date('Collection Date')