from odoo import models, fields, api
import logging


class PropertyActionWizard(models.TransientModel):
    _name='property.action.wizard'
    _description='Property Action Wizard'

    def action_save(self):
        _logger=logging.getLogger(__name__)
        _logger.info(f"inside button logic")
        _logger.info(f"Self:  ",self)

        active_id=self.env.context.get('active_id')
        _logger.info(f"active id =",active_id)
        if active_id:
            record=self.env['product.product'].browse(active_id)
            
            record.write({'state': 'available'})
        return {'type':'ir.actions.act_window_close'}
    
    def action_return(self):
        return {'type':'ir.actions.act_window',
                'res_model':'product.product',
                'view_mode':'form',
                'res_id':self.env.context.get('active_id'),
                'target':'current'
                }