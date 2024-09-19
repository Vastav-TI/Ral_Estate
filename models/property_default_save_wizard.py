from odoo import models,fields,api
import logging
class PropertySaveWizard(models.TransientModel):
    _name='property.save.wizard'
    _description='Property Save Confirmation Wizard'
    area=fields.Float('Area (sq meters)',required=True)
    msg=fields.Text('Message',readonly=True)
    list_price = fields.Float('Property Price', required=True)
    def confirm_save(self):
        # fetch active_id from context
        active_id=self.env.context.get('active_id')
        _logger=logging.getLogger(__name__)
        _logger.info(f"inside confirm button logic , active id-------{active_id}")
        _logger.info(f"Self -------{self}")
        _logger.info(f"Context -------{self.env.context}")

        if active_id:
            # browse property record using active id
            property_record=self.env['product.product'].browse(active_id)

            
            property_record.list_price=self.list_price
            
            property_record.area=self.area


            
            return {'type':'ir.actions.act_window_close'}
    
    


