# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'academy.teachers'
    # _description = 'academy.academy'

    name = fields.Char()
    biography = fields.Html()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100