# -*- coding: utf-8 -*-
{
    'name': "Lead Details",
    'summary': """It fetch the detail of a lead""",
    'description': """

=======================

This module show the details of the lead. When any lead update it shows, which field updated.
    """,
    'author': "Debasisa Dash",
    'website': "http://www.fdshive.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base','web','crm'],
    'data': [
        'view/lead_details_view.xml',
        'view/lead_detail_report.xml',
        'view/report_lead.xml',
        'security/ir.model.access.csv',
    ],

    'demo': [
        ],
    'installable':True,
    'auto_install':False,
}
