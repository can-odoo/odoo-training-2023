from odoo import models,fields,api

class franchiseOrder(models.Model):
    _inherit = "franchise.product.stock"

    payment = fields.Boolean()
    state = fields.Selection(selection=[('ordered','Ordered'),('shipped','Order Shipped'),('preparing','Preparing order'),('delivered', 'Delivered'),('canceled','Canceled')])


    @api.onchange('state')
    def _onchange_state(self):
        for record in self:
            record.status = "ordered"