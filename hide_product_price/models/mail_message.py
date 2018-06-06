# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Message(models.Model):
    _inherit = ['mail.message']

    msg_hide_track = fields.Boolean()
  