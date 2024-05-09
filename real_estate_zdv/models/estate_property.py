# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import api, models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "ZDV Estate Property (training model)"

    name = fields.Char('Name', required = True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability', default = datetime.today() + relativedelta(months=3), copy = False)
    expected_price = fields.Float('Expected Price', required = True)
    selling_price = fields.Float('Selling Price', readonly = True, copy = False)
    bedrooms = fields.Integer('Bedrooms', default = 2)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north', 'North'), 
                     ('south', 'South'), 
                     ('east', 'East'), 
                     ('west', 'West')],
        help = "Used to select orientation of the Garden"
        )
    active = fields.Boolean(default = True)
    state = fields.Selection(selection = 
                    [('new', 'New'), 
                     ('offer_received', 'Offer Received'), 
                     ('offer_accepted', 'Offer Accepted'), 
                     ('sold', 'Sold'), 
                     ('canceled', 'Canceled')],
                     default = 'new',
                     required = True,
                     copy = False)
    property_type_id = fields.Many2one("property.type", string="Type")

    buyers_id = fields.Many2one("res.partner", string="Buyer")
    salesmans_id = fields.Many2one("res.users", string="Salesman")

    tags = fields.Many2many("property.tags", string="Tags")

    offer_ids = fields.One2many("property.offer", "property_id", string="Offers")

    total_area = fields.Integer(string="Total Area", compute="_compute_total_area", readonly = True)

    best_price = fields.Float("Best Price", compute="_compute_best_offer", readonly = True)

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for record in self:
            prices = record.mapped('offer_ids.price')
            if len(prices)!=0:
                record.best_price = max(prices)
                continue
            record.best_price = 0
