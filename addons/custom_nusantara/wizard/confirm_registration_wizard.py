from odoo import models, fields

class ConfirmRegistrationWizard(models.TransientModel):
    _name = 'nusantara.confirm.registration.wizard'
    _description = 'Wizard Konfirmasi Pendaftaran'

    message = fields.Char(string='Pesan', default='Anda akan menambahkan catatan konfirmasi ke semua pendaftaran terpilih.')

    def action_confirm(self):
        active_ids = self.env.context.get('active_ids', [])
        registrations = self.env['nusantara.event.registration'].browse(active_ids)
        for reg in registrations:
            reg.notes = (reg.notes or '') + '\n[Dikonfirmasi via Wizard]'