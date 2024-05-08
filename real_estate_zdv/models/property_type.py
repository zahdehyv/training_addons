# -*- coding: utf-8 -*-

from odoo import models, fields

class PropertyType(models.Model):
    _name = "property.type"
    _description = "ZDV Property Types (training model)"

    name = fields.Char('Name', required = True)