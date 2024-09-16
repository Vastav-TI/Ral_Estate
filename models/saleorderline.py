# In your module's models file, e.g., models/sale_order_line.py

from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    description_purchase = fields.Text(
        related='product_id.description_purchase',
        string='Product Description',
        readonly=True
    )
