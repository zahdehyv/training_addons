# -*- coding: utf-8 -*-

from odoo import models, fields

class PropertyOffer(models.Model):
    _name = "property.offer"
    _description = "ZDV Property Offers (training model)"

    price=fields.Float("Price")
    status=fields.Selection(selection = [('accepted', 'Accepted'), ('refused', 'Refused')], string="Status", copy=False)
    partner_id = fields.Many2one("res.partner", string="Bidder", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)