from odoo import fields, models, Command

class cardekhoInvoice(models.Model):
    _inherit="car.dekho.property"
    
    def car_sold(self):
        res = super().car_sold()
        for record in self:
            self.env['account.move'].create({
                'partner_id':self.buyer_id.id,
                'move_type':'out_invoice',
                "invoice_line_ids":[
                    Command.create({
                        'name':record.car_name,
                        'quantity':1.0,
                        'price_unit':record.selling_price * 0.06
                    }),
                    Command.create({
                        'name':'Administrative fees',
                        'quantity':1.0,
                        'price_unit': 100.0
                    }),
                ]
            })
        return res