# -*- coding: utf-8 -*-
{
    "name": "hide product price",
    "summary": "Hide product pricing from Online quotation",
    "version": "11.0.1.0.0",
    "category": "Website",
    "author": "AgPack Inc, "
              "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "website","website_sale","sale",
    ],
    "data": [
        "security/hide_chatter_price_security.xml",
        "views/hide_product_price.xml",
    ],
}
