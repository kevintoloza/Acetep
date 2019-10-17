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
    product_ids = fields.One2many(comodel_name='prueba.prueba.producto', inverse_name='venta_id')
    producto = fields.Char(string="Producto")
    productocalculado= fields.Char()
     
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

class ventaproducto(models.Model):
    _name = 'prueba.prueba.producto'
    name = fields.Char(string="Codigo")
    product_id = fields.Many2one(comodel_name='product.product')
    producto = fields.Char(string="Producto", related='product_id.name' )
   # precio = fields.Float(string="Precio", related='product_id.price_unit')
    venta_id = fields.Many2one(comodel_name='prueba.prueba')

  