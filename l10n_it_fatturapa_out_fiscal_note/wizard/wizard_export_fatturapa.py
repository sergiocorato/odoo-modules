# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models

class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"

    def setDatiGeneraliDocumento(self, invoice, body):
        res = super(WizardExportFatturapa, self).setDatiGeneraliDocumento(invoice, body)
        if invoice.fiscal_position_id.note:
            body.DatiGenerali.DatiGeneraliDocumento.Causale = invoice.fiscal_position_id.note
        return res
