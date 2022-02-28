from odoo import api, fields, models


class stockDimension(models.Model):
    _inherit = "account.move.line"

    dimension = fields.Char(string='dimensions')

    # def _prepare_invoice_values(self, order, name, amount, so_line):
    #     res = super()._prepare_invoice_values(order, name, amount, so_line)
    #     res['invoice_line_ids'] = so_line.dimension
    #     return res


class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        res = super(StockRuleInherit, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id,
                                                                   name,
                                                                   origin, company_id, values)
        res['dimension'] = values.get('dimension', False)
        return res
