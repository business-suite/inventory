# -*- coding: utf-8 -*-


{
    'name': 'Units of measure',
    'version': '1.0',
    'category': 'Inventory/Inventory',
    'depends': ['base'],
    'description': """
This is the base module for managing Units of measure.
========================================================================
    """,
    'data': [
        'data/uom_data.xml',
        'security/uom_security.xml',
        'security/ir.model.access.csv',
        'views/uom_uom_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
