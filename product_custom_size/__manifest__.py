# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
# This is essentialy a copied version of product_brand

{
    'name': 'Product Size Manager',
    'version': '12.0.1.0.0',
    'category': 'Product',
    'summary': "Product Size Manager",
    'author': 'LP',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_size_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
