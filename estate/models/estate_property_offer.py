from odoo import api,models,fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is offer model contains the offers rais for perticular properties"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(selection =[('accepted','Accepted'),('refused','Refused')], copy=False)
    partner_id = fields.Many2one('res.partner',required = True)
    property_id = fields.Many2one('estate.property', required=True)
    property_type_id = fields.Many2one(related="property_id.property_type_id", store= True)
    validity = fields.Integer("Validity ( days )",default=7)
    deadline = fields.Date("Deadline",compute="_compute_deadline",default = fields.date.today(),inverse="_inverse_deadline")


    @api.depends('validity','create_date')
    def _compute_deadline(self):
        for record in self:
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
                            
    def action_accept(self):
        for record in self:
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id
            record.property_id.state="offer_accepted"

    def action_refused(self):
        for record in self:
            record.status = "refused"
            record.property_id.selling_price = 0
            record.property_id.buyer = 0

    _sql_constraints = [
        ('check_offer_price_1','CHECK(price > 0)','A offer price must be strictly positive'),
    ]