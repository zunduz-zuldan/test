{
    'name': 'Customer Management',
    'version': '1.0',
    'sequence': -100,
    'category': 'Sales',
    'author': 'Your Name',
    'description': 'Module for managing customer details.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/customer_details_tree_view.xml',
        'views/customer_details_form_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
