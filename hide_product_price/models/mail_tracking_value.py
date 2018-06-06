# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class MailTracking(models.Model):
    _inherit = ['mail.tracking.value']

    @api.model
    def create(self, vals):
        res = super(MailTracking, self).create(vals)
        if res.mail_message_id and res.mail_message_id.model == 'sale.order' and res.field in ['amount_untaxed','amount_tax','amount_total']:
            res.mail_message_id.msg_hide_track = True
        return res
