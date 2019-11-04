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

    @api.one
    @api.constrains('stage_id')
    def condicion(self):
        for r in self:
            if r.stage_id:
                if r.stage_id.requirements == 'contacto':
                    if not r.mobile:
                        raise ValidationError ('para pasar este estado se necesita que mobile este lleno')
                if r.stage_id.requirements == 'child':
                    if not r.nino_id:
                        raise ValidationError ('para pasar este estado se necesita que nino este lleno')


