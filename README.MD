# 🚀 QA Automation Tracker - Python & Playwright (POM)

Repositori ini digunakan sebagai jurnal belajar mandiri dan pelacak kemajuan (*progress tracker*) transisi dari QA Manual ke QA Automation menggunakan Python dan Playwright Framework dengan pendekatan *Page Object Model* (POM).

---

## 🏁 Checklist Pencapaian (Progress Tracker)

### 📚 MINGGU 1: Pondasi Pemrograman Python & Mindset Automation
- [x] Teori dasar Python (Variabel, Tipe Data, Logika Kondisi, Looping, & Function)
- [x] Praktik membuat logika sederhana Python
- [x] **Status:** `SELESAI` (Bawaan dasar kuliah & penyegaran internal)

### 🏗️ MINGGU 2: Object-Oriented Programming (OOP) & Arsitektur Folder
- [x] Pemahaman dasar *Class*, *Object*, dan *Methods* untuk kebutuhan POM
- [x] Implementasi struktur direktori bersih (`pages/` dan `tests/`)
- [x] **Status:** `SELESAI` (Struktur folder proyek sudah tertata rapi)

### 🎭 MINGGU 3: Playwright Core, Skenario Negatif & Reporting
- [x] Menghubungkan berkas tes lintas folder dengan struktur `from pages.login_page import LoginPage`
- [x] Membuat *Positive Case* & *Negative Case* di web SauceDemo
- [x] Integrasi laporan otomatis berformat `report.html` menggunakan `pytest-html`
- [x] Mengatasi kendala environment path (`$env:PYTHONPATH="."`) di terminal PowerShell
- [x] **Optimasi Conftest:** Konfigurasi *Headless Mode* (`headless=True`) di `conftest.py`
- [x] **Assert Lanjutan:** Validasi presisi teks pesan eror yang muncul di UI SauceDemo
- [x] **Status:** `SELESAI` 🎉

### 🚀 MINGGU 4: Advance UI Automation & Pengenalan CI/CD Pipeline
- [x] **Dynamic Element & Waiting Mechanism:** Menangani komponen web yang lambat memuat (*loading*)
- [x] **Data-Driven Testing (DDT):** Menguji banyak skenario negatif sekaligus menggunakan `@pytest.mark.parametrize`
- [x] **Git Integration:** Inisialisasi `git init`, konfigurasi `.gitignore` untuk menyaring folder `venv/`, dan melakukan *commit* pertama
- [x] **Status:**  `SELESAI` 🎉

---

## 📊 Hasil Eksekusi Terakhir (Benchmark)
* **Mode Running:** Headless Mode (True)
* **Status Pengujian:** 7 Passed ✅
* **Catatan Waktu Eksekusi:** 27.04s ⏱️