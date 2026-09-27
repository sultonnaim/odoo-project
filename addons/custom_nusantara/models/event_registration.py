from odoo import models, fields, api
from odoo.exceptions import ValidationError

class NusantaraEventRegistration(models.Model):
    _name = 'nusantara.event.registration'
    _description = 'Pendaftaran Event Nusantara'

    name = fields.Char(string='Nama Peserta', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='No. HP')
    partner_id = fields.Many2one('res.partner', string='Contact')
    registration_date = fields.Date(string='Tanggal Daftar', default=fields.Date.today)
    notes = fields.Text(string='Catatan')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.name = self.partner_id.name
            self.email = self.partner_id.email
            self.phone = self.partner_id.phone

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError('Format email tidak valid, harus mengandung "@".')
            
    @api.model
    def _cron_reminder_pendaftaran(self):
        registrations = self.search([('email', '=', False)])
        for reg in registrations:
            reg.notes = (reg.notes or '') + '\n[Reminder otomatis] Email peserta belum diisi.'