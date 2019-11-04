# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID


class Crmupdate(models.Model):
    _inherit = 'crm.lead'
    nino_id = fields.Many2one(comodel_name='acetep.nino', string="Niño")
    programastate = fields.Selection([('GYMBOREE','GYMBOREE'), ('Gymkids','GymKids'), ('Preschoolstep','Pre school step')], string="Cual programa ")
    contacto = fields.Char(string="Contacto")
    fechacita = fields.Date(string="Fecha de cita")

    @api.one
    @api.constrains('stage_id')
    def condicion(self):
        for r in self:
            if r.stage_id:
                if r.stage_id.requirements == 'ninocampo':
                    if not r.nino_id:
                        raise ValidationError ('Para pasar al estado previews se necesita que formulario del nino este lleno')
                if r.stage_id.requirements == 'mobile':
                    if not r.mobile:
                        raise ValidationError ('para pasar al estado reserva se necesita el movil del contacto')


