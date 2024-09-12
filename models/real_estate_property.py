from odoo import models, fields

class RealEstateProperty(models.Model):
    _inherit = 'product.product'

    name = fields.Char(string='Property Name', required=True)
    address = fields.Char('Property Address', required=True)
    type = fields.Selection([
        ('residential', 'Residential'),
        ('commercial', 'Commercial')    ], 
        string='Property Type', required=True)
    list_price = fields.Float('Property Price', required=True)
    area = fields.Float('Area (sq meters)')
    
    state = fields.Selection([
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('under_construction', 'Under Construction'),
        ('rented', 'Rented')  # Added 'Rented' option
    ], string='State', default='available')
    description_purchase=fields.Text('Description')
    image_128=fields.Binary('Property Image')
    owner_id = fields.Many2one('res.partner', string='Owner')