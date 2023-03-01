from odoo import api,models,fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is offer model contains the offers rais for perticular properties"

    price = fields.Float()
    status = fields.Selection(selection =[('accepted','Accepted'),('refused','Refused')], copy=False)
    partner_id = fields.Many2one('res.partner',required = True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer("Validity ( days )",default=7)
    deadline = fields.Date("Deadline",compute="_compute_deadline",default = fields.date.today(),inverse="_inverse_deadline")


    @api.depends('validity','create_date')
    def _compute_deadline(self):
        for record in self:
            print(record.create_date)
            if record.create_date:
                record.deadline = fields.Date.add(record.create_date.date(),days=record.validity)
            else :
                record.deadline = fields.Date.add(fields.date.today(),days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            if record.create_date:
                record.validity = (record.deadline-record.create_date.date()).days
            else :
                record.validity = (record.deadline-fields.date.today()).days
                            