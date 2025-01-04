{
    'name': 'School Management',
    'version': '1.0',
    'sequence': -100,
    'category': 'Sales',
    'author': 'Your Name',
    'description': 'Module for managing student in school.',
    'depends': ['base'],
    'data': [
        'security/student_security.xnl',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
