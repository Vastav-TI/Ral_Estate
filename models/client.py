from odoo import models, fields

class RealEstateClient(models.Model):
    _inherit = 'res.partner'

    is_client = fields.Boolean(string='Is Client', default=False)
    # purchase_history_ids = fields.One2many('real.estate.contract', 'client_id', string='Purchase History')
