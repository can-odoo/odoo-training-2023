from odoo import models,fields

class resUser(models.Model):
    _inherit = "res.users"

    # property_ids = fields.One2many('estate.property','salesman',domain=[('state','in',('new','offer_recieved'))])
    property_ids = fields.One2many('estate.property','salesman')

