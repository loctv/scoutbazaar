# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import Warning

class AccountPayment(models.Model):
    _inherit = 'account.payment'
        
    transfer_journal_id = fields.Many2one('account.journal','Transfer Journal')
    
    @api.multi
    def action_validate_invoice_payment(self):
        active_id = self._context.get('active_id')
        account_invoice = self.env['account.invoice'].browse(active_id)
        journal_entry_first = account_invoice.payment_journal_id
        if not journal_entry_first:
            account_invoice.write({'payment_journal_id':self.transfer_journal_id.id})
        elif account_invoice.payment_journal_id == self.transfer_journal_id:
            return super(AccountPayment,self).action_validate_invoice_payment()
        else:
            raise Warning(_("Transfer Journal not to change. (%s) to select in transfer journal")%account_invoice.payment_journal_id.name)
        
        return super(AccountPayment,self).action_validate_invoice_payment()
    
class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    payment_journal_id = fields.Many2one('account.journal','Payment Journal')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    shipping_charge = fields.Float("Shipping Charge")
    extra_charge_product = fields.Float("Extra Charge")
    
class ResPatner(models.Model):
    _inherit = 'res.partner'
    
    child_account_id = fields.Many2one('account.account','Account')
