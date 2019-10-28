# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID

class Crmupdate(models.Model):
    _inherit = 'crm.lead'
    nino_id = fields.Many2one(comodel_name='acetep.nino', string="Niño")

