from odoo import models, fields

class RealEstateClient(models.Model):
    _inherit = 'res.partner'

    # name=fields.Char(string="owner Name")
    is_owner = fields.Boolean(string='Is Owner', default=False,required=True)
    # partner_type = fields.Selection([
    #     ('client', 'Client'),
    #     ('owner', 'Owner'),
    #     ('tenant', 'Tenant')
    # ], string='Partner Type', default='client')
    owned_property_ids = fields.One2many('product.product', 'owner_id', string='Owned Properties')
    # purchase_history_ids = fields.One2many('real.estate.contract', 'client_id', string='Purchase History')
