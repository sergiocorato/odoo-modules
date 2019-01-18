# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Italian Localization - Contabilità Minimale',
    'version': '10.0.1.0.1',
    'depends': ['base_vat','base_iban'],
    'author': 'SC & LP',
    'category': 'Localization/Italy',
    'license': 'AGPL-3',
    'description': """
Piano dei conti minimale.
================================================

Italian accounting chart and localization.
    """,
    'data': [
        'data/l10n_it_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.tax.template.csv',
        'data/account.fiscal.position.template.csv',
        'data/account.fiscal.position.tax.template.csv',
        'data/account.chart.template.csv',
        'data/account_chart_template_data.yml',
        ],
}
