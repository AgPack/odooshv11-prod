# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, http
from odoo.http import request
from odoo.addons.website_quote.controllers.main import sale_quote


class sale_quote(sale_quote):

    @http.route("/quote/<int:order_id>/<token>", type='http', auth="public", website=True)
    def view(self, order_id, pdf=None, token=None, message=False, **post):
        now = fields.Date.today()
        if token:
            Order = request.env['sale.order'].sudo().search([('id', '=', order_id), ('access_token', '=', token)])
        else:
            Order = request.env['sale.order'].search([('id', '=', order_id)])
        # Log only once a day
        if Order and request.session.get('view_quote') != now and request.env.user.share:
            request.session['view_quote'] = now
            body = _('Quotation viewed by customer')
            _message_post_helper(res_model='sale.order', res_id=Order.id, message=body, token=token, message_type='notification', subtype="mail.mt_note", partner_ids=Order.user_id.sudo().partner_id.ids)
        if not Order:
            return request.render('website.404')

        # Token or not, sudo the order, since portal user has not access on
        # taxes, required to compute the total_amout of SO.
        order_sudo = Order.sudo()

        if pdf:
            pdf = request.env.ref('website_quote.report_web_quote').with_context(set_viewport_size=True).render_qweb_pdf([order_sudo.id])[0]
            pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
            return request.make_response(pdf, headers=pdfhttpheaders)
        return super(sale_quote, self).view(order_id, pdf=None, token=None, message=False, **post)

