# -*- coding: utf-8 -*-
{
    'name': "account_bolivia_lector_qr",

    'summary': """
        Lector QR para cargar más rápido las compras en Bolivia""",

    'description': """
        Lector QR para cargar más rápido las compras en Bolivia
    """,

    'author': "Sistecem",
    'website': "https://sistecem.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['codigodecontrolbolivia','web_camera_qrcode_widget'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
