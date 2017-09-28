# -*- coding: utf-8 -*-
# Copyright (C) 2017 Creu Blanca
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'POS Pay invoice',
    'version': '10.0.1.2.0',
    'category': 'Point Of Sale',
    'sequence': 1,
    'author': "Creu Blanca,"
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/pos',
    'summary': 'Pay and receive invoices from PoS Session',
    'depends': [
        "point_of_sale",
    ],
    'data': [
        "wizard/pos_invoice_in.xml",
        "wizard/pos_invoice_out.xml",
        "views/pos_session.xml",
    ],
}
