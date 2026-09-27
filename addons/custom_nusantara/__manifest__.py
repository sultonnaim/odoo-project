{
    'name': 'Nusantara Kreatif Custom',
    'version': '1.0',
    'summary': 'Custom module untuk PT Nusantara Kreatif Group',
    'description': 'Module custom untuk fitur tambahan spesifik bisnis',
    'author': 'Nama Kamu',
    'category': 'Customization',
    'depends': ['base', 'crm', 'sale'],
    'data': [
    'security/ir.model.access.csv',
    'views/event_registration_views.xml',
    'views/crm_lead_view_inherit.xml',
    'data/ir_cron_data.xml',
    'wizard/confirm_registration_wizard_views.xml',
],
    'installable': True,
    'application': False,
}