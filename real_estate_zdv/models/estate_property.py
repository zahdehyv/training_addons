# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields

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
