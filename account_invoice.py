from openerp import api, fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.multi
    @api.returns('self')
    def refund(self, date_invoice=None, date=None, description=None, journal_id=None):
        """
        For a financial refund we need to check the line GL accounts created from the source document - 
        if the souce GL is an input/output account we will default to income/expense account
        as there will never be a stock move to offset to.

        """
        new_invoices = super(AccountInvoice, self).refund(date_invoice, date, description, journal_id)
        for invoice in new_invoices:
            for line in invoice.invoice_line_ids:
                if line.product_id:
                    expense_account = line.product_id.categ_id.property_account_expense_categ_id or line.product_id.property_account_expense_id
                    income_account = line.product_id.categ_id.property_account_income_categ_id or line.product_id.property_account_income_id
                    input_account = line.product_id.categ_id.property_stock_account_input_categ_id or line.product_id.property_stock_account_input
                    output_account = line.product_id.categ_id.property_stock_account_output_categ_id or line.product_id.property_stock_account_output

                    if invoice.type in ('in_invoice', 'in_refund') and line.account_id.id in (input_account.id, output_account.id):
                        line.write({'account_id': expense_account.id})
                    elif invoice.type in ('out_invoice', 'out_refund') and line.account_id.id in (input_account.id, output_account.id):
                        line.write({'account_id': income_account.id})

        return new_invoices
