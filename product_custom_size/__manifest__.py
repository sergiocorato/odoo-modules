# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
# This is essentialy a copied version of product_brand

{
    'name': 'Product Size Manager',
    'version': '10.0.1.0.1',
    'category': 'Product',
    'summary': "Product Size Manager",
    'author': 'LP',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        ],
    'data': [
        'views/product_size_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': False,
}
