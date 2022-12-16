# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'CRM',
    'version': '15.0.1.0.0',
    'category': 'Sales/CRM',
    'sequence': 1,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'website': 'https://www.odoo.com/app/crm',
    'depends': ['crm'],
    'data': [
        'data/crm_stage.xml',
        'views/crm_views.xml',
        'views/res_partner_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}
