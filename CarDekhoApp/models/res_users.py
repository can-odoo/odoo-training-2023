from odoo import fields, models

class res_users(models.Model):
    _inherit="res.users"
    property_ids=fields.One2many('car.dekho.property','user_id',domain=[('state','in',['new','offer_received'])])