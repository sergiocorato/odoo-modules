# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class ProductSize(models.Model):
    _name = 'product.size'

    name = fields.Char('Size', required=True)
    description = fields.Text('Description', translate=True)
    graphic = fields.Binary('Graphic File')
    product_ids = fields.One2many(
        'product.template',
        'product_size_id',
        string='Size Products',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )

    @api.one
    @api.depends('product_ids')
    def _get_products_count(self):
        self.products_count = len(self.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_size_id = fields.Many2one(
        'product.size',
        string='Size',
        help='Select a size for this product'
    )
