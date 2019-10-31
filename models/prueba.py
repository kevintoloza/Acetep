# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID

class venta(models.Model):
    _name = 'prueba.prueba'
    name = fields.Char(string="Nombre")
    codigo = fields.Char(string="Codigo")
    partner_id = fields.Many2one(comodel_name='res.partner' , string="Cliente", compute='_on_change_dom' )
    product_ids = fields.One2many(comodel_name='prueba.prueba.producto', inverse_name='venta_id', string="Productos")
    producto = fields.Char(string="Producto")
    productocalculado= fields.Char()
    
    @api.one
    def procesar(self):
        for r in self:
            order = self.env['sale.order'].create({'name': r.partner_id.name,'partner_id': r.partner_id.id,'date_order': datetime.now()})
            for l in r.product_ids:
                line = self.env['sale.order.line'].create({'name': l.producto, 'order_id': order.id,'price_unit': l.product_id.list_price,'product_id':l.product_id.id})
      
     
    @api.one
    @api.depends('codigo')
    def _on_change_dom(self):
        if self.codigo:
            line = self.env['res.partner'].search([('mobile', '=', self.codigo)],limit=1)
            if line:
                self.partner_id = line.id 
                
   
    @api.one
    def addProducto(self):
        for r in self:
            if r.producto:
                line = self.env['product.product'].search([('barcode', '=', r.producto)],limit=1)
                if line:
                    x=self.env['prueba.prueba.producto'].create({'name': r.producto,'product_id': line.id,'venta_id': r.id})
                r.producto=None

    @api.multi
    def action_quotation_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('Acetep', 'email_template_edi_sale')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = {
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
   
                

class ventaproducto(models.Model):
    _name = 'prueba.prueba.producto'
    name = fields.Char(string="Codigo")
    product_id = fields.Many2one(comodel_name='product.product', string="Descripcion")
    producto = fields.Char(string="Producto", related='product_id.name' )
   #precio = fields.Float(string="Precio", related='product_id.price_unit')
    venta_id = fields.Many2one(comodel_name='prueba.prueba')

