from odoo import fields,models,Command

class estateProperty(models.Model):
    _inherit="estate.property"
    
    def action_sold(self):
        self.env['account.move'].create({
            'partner_id':self.buyer.id,
            'move_type':"in_refund",
            'invoice_line_ids':[
                Command.create({
                    'name':'Brokerage',
                    'quantity':1,
                    'price_unit':0.06*self.selling_price
                }),
                Command.create({
                    'name':'administrative fees',
                    'quantity':1,
                    'price_unit':100
                })
            ]
        })
        return super().action_sold()