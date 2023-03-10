from odoo import fields, models, Command

class RecurringPlan(models.Model):
    _inherit="estate.recurring.plan"
    
    def set_sold(self):
        res = super().set_sold()
        for record in self:
            self.env['account.move'].create({
                'partner_id':self.buyer_id.id,
                'move_type':'out_invoice',
                "invoice_line_ids":[
                    Command.create({
                        'name':record.name,
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