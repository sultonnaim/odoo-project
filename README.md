# PT Nusantara Kreatif Group — Odoo ERP Implementation

Project simulasi implementasi Odoo ERP untuk sebuah grup usaha fiktif (PT Nusantara Kreatif Group) yang bergerak di bidang merchandise custom, jasa desain grafis, dan penjualan online. Project ini dibuat sebagai portofolio pembelajaran end-to-end Odoo — mulai dari konfigurasi fungsional lintas modul, deployment via Docker, hingga pengembangan custom module dari nol.

## 📋 Latar Belakang

PT Nusantara Kreatif Group adalah studi kasus bisnis dengan beberapa lini usaha:
- **Merchandise & Retail** — produksi dan penjualan kaos custom, totebag
- **Jasa Kreatif** — layanan desain grafis (logo, kemasan, katalog)
- **Online Store** — penjualan produk melalui eCommerce
- **Event & Training** — workshop dan pelatihan

Skenario ini dipilih agar hampir seluruh modul Odoo dapat dieksplorasi secara alami dalam satu alur bisnis yang koheren, bukan sekadar mencoba fitur secara terpisah.

## 🛠️ Tech Stack

- **Odoo 18.0** (Community Edition)
- **PostgreSQL 15**
- **Docker & Docker Compose**
- **VS Code** sebagai development environment
- **Navicat** untuk database inspection

## 🚀 Cara Menjalankan Project

### Prasyarat
- Docker Desktop terinstall dan berjalan
- Git

### Langkah Instalasi

```bash
# Clone repository
git clone https://github.com/USERNAME/odoo-nusantara-kreatif.git
cd odoo-nusantara-kreatif

# Jalankan container
docker compose up -d

# Cek status container
docker compose logs -f odoo
```

Tunggu hingga log menunjukkan `HTTP service (werkzeug) running on 0.0.0.0:8069`, lalu buka browser ke `http://localhost:8069` dan buat database baru.

### Struktur Docker Compose

| Service | Image | Port |
|---|---|---|
| `db` | postgres:15 | 5432 |
| `odoo` | odoo:18.0 | 8069 |

## 📦 Modul yang Dieksplorasi

### Core Business Flow
- [x] **CRM** — pipeline lead, kualifikasi, won/lost, activity tracking
- [x] **Sales** — quotation, sales order, invoicing policy (ordered vs delivered)
- [x] **Purchase** — RFQ, purchase order, receipt
- [x] **Inventory** — stock tracking, delivery order, on hand quantity
- [x] **Manufacturing** — Bill of Materials (BoM), Manufacturing Order
- [x] **Accounting/Invoicing** — invoice, payment registration
- [x] **Point of Sale** — kasir, transaksi cash, tutup sesi

### Channel & Marketing
- [x] **Website Builder** — landing page, halaman About Us
- [x] **eCommerce** — publish produk, checkout end-to-end, integrasi ke Sales Order
- [x] **Email Marketing** — campaign promosi
- [x] **Events** — pendaftaran peserta, tiket digital
- [x] **eLearning** — course online dengan materi bertahap

### Operasional & HR
- [x] **Project & Timesheet** — task management, pencatatan jam kerja
- [x] **Employees** — data karyawan, departemen
- [x] **Recruitment** — proses rekrutmen dari lowongan hingga kandidat
- [x] **Time Off** — pengajuan dan approval cuti
- [x] **Expenses** — klaim reimbursement karyawan
- [x] **Fleet** — kendaraan operasional
- [x] **Discuss** — komunikasi internal

### Fitur Enterprise (tidak tersedia di Community, dipahami secara teori)
- Helpdesk, Appointments, Approvals, Knowledge, Sign

## 💻 Custom Module Development

Selain eksplorasi fungsional, project ini juga mencakup pengembangan module custom dari nol: **`custom_nusantara`**.

### Struktur Module

```
custom_nusantara/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── event_registration.py      # Model baru: Pendaftaran Event
│   └── crm_lead_inherit.py         # Inherit model CRM Lead
├── views/
│   ├── event_registration_views.xml
│   └── crm_lead_view_inherit.xml
├── wizard/
│   ├── __init__.py
│   ├── confirm_registration_wizard.py
│   └── confirm_registration_wizard_views.xml
├── security/
│   └── ir.model.access.csv
└── data/
    └── ir_cron_data.xml
```

### Fitur yang Diimplementasikan

- **Model baru** (`nusantara.event.registration`) dengan field dasar dan relasi Many2one ke `res.partner`
- **View custom** (form & list) beserta menu baru di UI Odoo
- **Business logic**:
  - `@api.onchange` — auto-fill data saat memilih contact
  - `@api.constrains` — validasi format email
- **Model inheritance** — menambahkan field custom di `crm.lead` tanpa mengubah source code asli
- **Scheduled Action (Cron)** — reminder otomatis untuk data yang belum lengkap
- **Wizard (TransientModel)** — popup konfirmasi untuk aksi bulk

### Cara Update Module Setelah Perubahan Kode

```bash
docker exec -it odoo-nusantara-kreatif-odoo-1 odoo -u custom_nusantara -d nusantara_kreatif \
  --db_host=db --db_user=odoo --db_password=odoo --db_port=5432 --stop-after-init

docker compose restart odoo
```

## 📸 Screenshot

Screenshot alur utama tersedia di folder [`/screenshots`](./screenshots):
- CRM Pipeline
- Sales Order & Invoicing
- Inventory Delivery & Stock
- Manufacturing BoM
- eCommerce Checkout
- Custom Module Development

## 🎥 Video Demo

[Link video demo] — menunjukkan alur end-to-end dari CRM hingga custom module development.

## 📝 Catatan Pembelajaran

Beberapa kendala teknis yang ditemukan dan solusinya selama pengerjaan project ini:

- **Konflik port PostgreSQL** dengan Windows service native — diselesaikan dengan menonaktifkan service lokal atau mengganti port host di `docker-compose.yml`
- **Track Inventory tidak bisa diubah** setelah produk pernah digunakan dalam transaksi — solusinya membuat produk baru dengan konfigurasi yang benar sejak awal
- **View inherit error** (`field is undefined`) — disebabkan file model baru belum ter-import di `__init__.py`, sehingga field custom tidak terdaftar meski file XML view berhasil dimuat
- **Cache registry Odoo** kadang memerlukan restart penuh (`docker compose restart odoo`) setelah upgrade module, tidak cukup hanya command `-u` saja

## 👤 Author

[Nama Kamu] — Mahasiswa Informatika, project portofolio pembelajaran Odoo ERP

## 📄 License

Project ini dibuat untuk keperluan pembelajaran dan portofolio pribadi.