# -*- coding: utf-8 -*-

{
    "name": "Acetep",
    "category": '',
    "summary": """
     Mantenimiento acetep y configuracion .""",
    "description": """
	   Mantenimiento y configuracion

    """,
    "sequence": 1,
    "author": "Strategi-k",
    "website": "http://strategi-k.com",
    "version": '12.0.0.4',
    "depends": ['account','hr','account_asset'],
    "data": [
     
     'security/ir.model.access.csv',
     'views/acetep.xml',
     'views/partner.xml',
     'views/factura.xml'
    ],
    "installable": True,
    "application": True,
    "auto_install": False,

}
