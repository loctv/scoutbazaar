
from odoo import fields,models,_,api

class ShippingRates(models.Model):

    _name = 'shipping_rates'  
    _description = 'Shipping rate contains all data related to shipping from source to destination'
     
    name = fields.Char(string='Name', compute='_compute_name')
    source_country = fields.Many2one('res.country', string='Source Country')
    destination_country = fields.Many2one('res.country', string='Destination Country')
    delivery_carrier = fields.Selection(
    	[('delivery_carrier_1', 'Delivery Carrier 1'), ('delivery_carrier_2', 'Delivery Carrier 2'), ('delivery_carrier_3', 'Delivery Carrier 3'), ('delivery_carrier_4', 'Delivery Carrier 4')],
    	string='Delivery Carrier')
    min_weight = fields.Float(string='Minimum Weight')
    max_weight = fields.Float(string='Maximum Weight')
    is_active = fields.Boolean(default=False, string='Covid status / service available or not')
    rate = fields.Float('Rate', required=True)
    
    @api.depends('name')
    def _compute_name(self):
        for ship_rate in self:
            if self.source_country and self.destination_country:
                self.name = str(self.source_country.name) + '-' + str(self.destination_country.name) + '(' +  str(self.min_weight) + '-' +  str(self.max_weight) + ')gm'
    