# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID

class Nivel(models.Model):
    _name = 'acetep.nivel'
    name = fields.Char(string='Nombre')

class Seccion(models.Model):
    _name ='acetep.seccion' 
    name = fields.Char(string='Nombre')
    horario = fields.Char(string='Horario')
    nivel_id = fields.Many2one(comodel_name='acetep.nivel', string='Nivel')


class Periodo(models.Model):
    _name = 'acetep.periodo'
    name = fields.Char(string='Nombre')

class Partersv(models.Model): #cliente padre
    _inherit = 'res.partner'
    nino_id = fields.One2many(comodel_name='acetep.nino', inverse_name='partner_id' )
  

class Nino(models.Model):
    _name = 'acetep.nino'
    _inherit= ['mail.thread']
    _description='Informacion del niño'
    name = fields.Char(string='Nombre',track_visibility=True)
    birthday = fields.Date(string="Fecha de Nacimiento",track_visibility=True)
    partner_id = fields.Many2one(comodel_name='res.partner' ,string='Padre', track_visibility=True) #Nombre del padre
    employed_id = fields.Many2one(comodel_name='hr.employee' ,string='Instructora de la clase de prueba', track_visibility=True)
    datetest = fields.Date(string="Fecha de la clase de prueba", track_visibility=True)
    how = fields.Selection([('Redes sociales','Redes sociales'), ('Referido','Referido'), ('Familiar','Familiar'), ('Pagina web','Pagina web'),  ('Pasaba por el local','Pasaba por el local'), ('Alianza','Alianza'), ('Otros','Otros')], string="Como se entero?",track_visibility=True)
    claseprueba = fields.Selection([('Si','Si'), ('No','No')],string="Toma clase de prueba?", track_visibility=True)
    programastate = fields.Selection([('Gymboree','Gymboree'), ('Gymkids','GymKids'), ('Preschoolstep','Pre school step')], string="Cual programa viene?", track_visibility=True)
    nivel_id = fields.Many2one(comodel_name='acetep.nivel', string="Nivel", track_visibility=True)
    recorrido = fields.Many2one(comodel_name='hr.employee', string="Quien realizo el recorrido?", track_visibility=True)
    fecharecorrido = fields.Date(string="Fecha recorrido", track_visibility=True)
    sexo = fields.Selection([('Masculino','Masculino'), ('Femenino','Femenino')],string="Genero", track_visibility=True)



class Invoice(models.Model):
    _inherit='account.invoice.line'
    nino_id = fields.Many2one(comodel_name='acetep.nino', string='Niño')
    nivel_id =fields.Many2one(comodel_name='acetep.nivel', string='Nivel')
    seccion_id =fields.Many2one(comodel_name='acetep.seccion', string='seccion')
    periodo_id =fields.Many2one(comodel_name='acetep.periodo', string='periodo')

class Invoiceline(models.Model):
    _inherit='account.invoice' 
    facturade=fields.Char(string="Factura a nombre de ")


class Employed(models.Model):
    _inherit='hr.employee'
    nino_id = fields.One2many(comodel_name='acetep.nino', inverse_name='employed_id' )    
      