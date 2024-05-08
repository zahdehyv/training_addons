# -*- coding: utf-8 -*-

from odoo import models, fields

class PropertyTags(models.Model):
    _name = "property.tags"
    _description = "ZDV Property Tags (training model)"

    name = fields.Char('Name', required = True)