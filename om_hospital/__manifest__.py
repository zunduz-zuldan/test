{
'name': 'Hospital Managemet',
'version': '1.0.0',
'sequence': -100,
'author': 'zuzan',
'website': 'www.zuzan.com',
'category': 'health',
'summary': 'hospital management system',
'description': 'hospital management system',
'depends': ['mail','product'],
'data': [
    'security/ir.model.access.csv',
     'data/patient_tag_data.xml',
    'data/patient.tag.csv',
    'data/sequence_data.xml',
    'wizard/cancel_appointment_view.xml',
    'views/menu.xml',
    'views/patient_view.xml',
    'views/female_patint_view.xml',
    'views/appointment_view.xml',
    'views/patient_tag_view.xml',
    'views/odoo_playGround.xml',

],
'demo': [],
'application':True,
'license': 'LGPL-3',

}