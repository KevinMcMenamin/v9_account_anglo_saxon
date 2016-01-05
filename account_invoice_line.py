from openerp import api, fields, models
from openerp.tools.float_utils import float_compare
import openerp.addons.decimal_precision as dp


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    ###########################################################################
    #
    # - Fields
    #
    ###########################################################################

    cost_price = fields.Float(string="Cost Price", digits_compute=dp.get_precision("Account"))
    stock_move_id = fields.Many2one(comodel_name="stock.move", string="Stock Move")

    """
    If no purchase_line_id/sale_line_ids or move_id then do not change the defaulted acccount
    """

    def get_invoice_line_account(self, type, product, fpos, company):
        if company.anglo_saxon_accounting and product and product.type in ('consu', 'product'):
            accounts = product.product_tmpl_id.get_product_accounts(fiscal_pos=fpos)
            if type in ('in_invoice', 'in_refund') and not (self.purchase_line_id or self.stock_move_id):
                return accounts['expense']
            elif type in ('out_invoice', 'out_refund') and not (self.sale_line_ids or self.stock_move_id):
                return accounts['income']
        else:
            return super(AccountInvoiceLine, self).get_invoice_line_account(type, product, fpos, company)

    def _get_anglo_saxon_price_unit(self):
        self.ensure_one()
        res = super(AccountInvoiceLine, self)._get_anglo_saxon_price_unit()
        if self.cost_price:
            return self.cost_price
        elif self.stock_move_id and self.stock_move_id.price_unit:
            return self.stock_move_id.price_unit
        else:
            return self.product_id.standard_price


class account_invoice(models.Model):
    _inherit = "account.invoice"

    """
    for a financial invoice or credit (also known as a memo invoice/credit)
    there will never be a stock move and there is no Cost of Sale entry required
    """

    @api.model
    def _anglo_saxon_sale_move_lines(self, i_line):
        if not (i_line.sale_line_ids or i_line.stock_move_id):
            return []
        else:
            res = super(account_invoice, self)._anglo_saxon_sale_move_lines(i_line)
            return res
