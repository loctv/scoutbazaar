from odoo import api, models, fields, _
from odoo.exceptions import UserError
class ProductProduct(models.Model):
    
    _inherit = 'product.product'
    
    
    nso_partner_id = fields.Many2one('res.partner',string="NSO Partner",domain="[('is_nso','=',True)]")
    



    
    
    @api.multi
    def write(self,vals):
        res = super(ProductProduct,self).write(vals)
        if 'nso_partner_id' in vals:
            nso_partner = vals['nso_partner_id']
            stock_location = self.env['stock.location'].sudo().search([('nso_location_id','=',nso_partner)])
            if not stock_location:
                raise UserError('No store location found! Go to Scout Bazaar/NSO Stores Locations and configure it.')
            if stock_location:
                stock_scout = self.env['scout.stock'].sudo().search([('location_id','in',stock_location.ids)])
                if not stock_scout:
                    raise UserError("No NSO Stock Location! Go to Scout Bazaar/Configuration/NSO Stock Locations and configure it.")
        
        