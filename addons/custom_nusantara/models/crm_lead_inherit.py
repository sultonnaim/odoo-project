from odoo import models, fields

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    nusantara_event_registration_id = fields.Many2one(
        'nusantara.event.registration',
        string='Terkait Pendaftaran Event'
    )