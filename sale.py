from openerp import api, fields, models


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    @api.multi
    def _prepare_invoice_line(self, qty):

        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res.update({'cost_price': self.purchase_price})
        return res
