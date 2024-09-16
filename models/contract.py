# from odoo import models, fields
# class RealEstateContract(models.Model):
#     _name = 'real.estate.contract'
#     _description = 'Real Estate Contract'
#     contract_type = fields.Selection([
#         ('sale', 'Sale'),
#         ('lease', 'Lease'),
#         ('rent', 'Rent')
#     ], string='Contract Type', required=True)
#     start_date = fields.Date('Start Date', required=True)
#     end_date = fields.Date('End Date')
#     property_id = fields.Many2one('real.estate.property', string='Property', required=True)
#     client_id = fields.Many2one('res.partner', string='Client', required=True)
#     amount = fields.Float('Amount', required=True)
#     status = fields.Selection([
#         ('draft', 'Draft'),
#         ('active', 'Active'),
#         ('completed', 'Completed')
#     ], string='Status', default='draft')
#     agent_id = fields.Many2one('res.partner', string='Agent')
#     commission = fields.Float('Commission')

from odoo import models,fields
 
 
class SaleOrder(models.Model):
    _inherit='sale.order'
    description_purchase = fields.Text(related='order_line.product_id.description_purchase', string="Purchase Description")