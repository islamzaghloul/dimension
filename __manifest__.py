# -*- coding: utf-8 -*-
{
    'name': "dimension",
    'summary': """dimension""",
    'sequence': 10,
    'description': """Long description of module's purpose""",
    'website': "http://www.yourcompany.com",
    'category': 'Purchase',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['sale', 'stock', 'account'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stockDimension.xml',
        'views/invoiceDimension.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
