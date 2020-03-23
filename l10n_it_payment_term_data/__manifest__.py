# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Italian Localization - Termini di pagamento comuni',
    'version': '11.0.1.0.0',
    'category': 'Localization/Italy',
    'author': 'SC & LP',
    'license': 'AGPL-3',
    'depends': [
        'account_payment_term_extension',
        'l10n_it_fiscal_payment_term',
    ],
    'data': [
        'data/payment_data.xml',
    ],
    'installable': True,
}
