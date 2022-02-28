from odoo import api, fields, models


class stockDimension(models.Model):
    _inherit = "stock.move"

    dimension = fields.Char(string='dimensions')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        res.update({'dimension': self.dimension})
        return res

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({'dimension': self.dimension})
        return res


class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'
    dimension = fields.Char(string='Dimension:')

    def action_confirm(self):
        res = super(CustomSaleOrder, self).action_confirm()
        return res
