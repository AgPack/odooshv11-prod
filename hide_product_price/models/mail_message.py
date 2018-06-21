# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Message(models.Model):
    _inherit = "mail.message"

    @api.model
    def _message_read_dict_postprocess(self, messages, message_tree):
        """
            The purpose of overriding this method is to, hide some tracking field
            on chatter to specific group of user

            i.e total amount value on quotation, user other than manager should not be able to see

            This is the method where messages data is prepare for webclient, so here we filter out
            the tracking value based on the 'msg_hide_track' field which we set on create of tracking
            for the user other than manager

            TODO: may be we can get rid of this method, if we could have implement the search method
                of tracking value.
        """

        res = super(Message, self)._message_read_dict_postprocess(messages, message_tree)
        if self.user_has_groups('sales_team.group_sale_manager'):
            return res
        for msg in messages:
            tracking_ids = [t['id'] for t in msg['tracking_value_ids']]
            track_to_display_ids = self.env['mail.tracking.value'].sudo().search([('id', 'in', tracking_ids), ('msg_hide_track', '=', False)]).ids
            msg['tracking_value_ids'][:] = [d for d in msg['tracking_value_ids'] if d.get('id') in track_to_display_ids]
        return res
