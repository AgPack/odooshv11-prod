# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

STOP_TRACKING_FIELDS = ['amount_untaxed','amount_tax','amount_total']

class MailTracking(models.Model):
    _inherit = 'mail.tracking.value'

    msg_hide_track = fields.Boolean('Message Price Hide')

    @api.model
    def create(self, vals):
        res = super(MailTracking, self).create(vals)
        if res.mail_message_id and res.mail_message_id.model == 'sale.order' and res.field in STOP_TRACKING_FIELDS:
            res.msg_hide_track = True
        return res
