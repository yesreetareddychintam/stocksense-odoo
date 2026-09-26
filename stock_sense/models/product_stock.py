from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_stock_level = fields.Float(string='Minimum Stock Level', default=5.0)
    is_low_stock = fields.Boolean(string='Low Stock', compute='_compute_is_low_stock', store=True)

    @api.depends('qty_available', 'minimum_stock_level')
    def _compute_is_low_stock(self):
        for product in self:
            product.is_low_stock = product.qty_available < product.minimum_stock_level