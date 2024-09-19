from odoo import models, fields, api,_
import logging
class RealEstateProperty(models.Model):
    
    _inherit = 'product.product'

    # Property details
    address = fields.Char('Property Address', required=True)
    type = fields.Selection([
        ('residential', 'Residential'),
        ('commercial', 'Commercial')], 
        string='Property Type', required=True)
    list_price = fields.Float('Property Price', required=True)
    area = fields.Float('Area (sq meters)')
    
    state = fields.Selection([
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('under_construction', 'Under Construction'),
        ('rented', 'Rented')],  # Added 'Rented' option
        string='State', default='available')
    
    description_purchase = fields.Text('Description')
    image_1920 = fields.Binary('Property Image')
    owner_id = fields.Many2one('res.partner', string='Owner')
    Is_property = fields.Boolean(string="Is Property", default=False, required=True)

    # New field for unique property ID
    property_id = fields.Char(string='Property ID', readonly=True)

    
    def action_open_save_wizard(self):
        self.ensure_one()
        _logger=logging.getLogger(__name__)
        _logger.info(f"self: {self}")
        
        if True:
            # open the confirmation wizard
            return {
                'name':_('Confirm Save with Default Values'),
                'type':'ir.actions.act_window',
                'res_model':'property.save.wizard',
                'view_mode':'form',
                'target':'new',
                'context':{'default_msg': 'Set The Area and Price'
                    ,'default_list_price': 200000, 'default_area': 220
                    } 
            }
        else:
            self.write({
                'list_price': self.list_price,
                'area': self.area
            })
            return {'type': 'ir.actions.act_window_close'}
    
    def get_context(self):
        _logger=logging.getLogger(__name__)
        _logger.info(f"self: {self}")
        _logger.info(f"contex-----------------{self.env.context}")




        
    
    
    # Override the create method to assign unique property_id
    @api.model
    def create(self, vals):
        _logger=logging.getLogger(__name__)
        _logger.info(f"self {self}")
        _logger.info(f"vals {vals}")
        

        
        # Check if the record is a property and property_id is not already set
        if vals.get('Is_property', False) and not vals.get('property_id'):
            # Count the number of properties with is_property=True
            count = self.search_count([('Is_property', '=', True)])
            # Generate the next sequence for property_id
            next_seq = count + 1
            vals['property_id'] = 'PROP{:03d}'.format(next_seq)
            
        # Call the original create method with updated vals
        result=super(RealEstateProperty, self).create(vals)
        _logger.info(f"result---------{result}")
        return result
    
    @api.model
    def write(self, vals):
        _logger=logging.getLogger(__name__)
        _logger.info(f"self------------ {self}")
        _logger.info(f"vals----------- {vals}")
        

        
        vals['name']=self.name.capitalize()
        result = super(RealEstateProperty, self).write(vals)
        _logger.info(f" updated result -------------{result}")
        _logger.info(f" updated vals ----------------{vals}")
        # Check if the record is a property and property_id is not already set
        

        return result
