# Release Notes - Universal Spam Chat Bot for Multi-Line Messages (Android USB Debugging)

**🚀 Versi 2.0.0 (Multi-Line Messages)**
**📅 Release Date**: 2025-04-19

---

## ✨ Fitur Utama Baru

- **Multi-pesan teks** (tidak terbatas jumlahnya)
- **Antarmuka interaktif** dalam Bahasa Indonesia
- **Escape karakter otomatis** untuk karakter khusus
- **Optimasi kecepatan** pengiriman pesan

---

## 📦 Komponen

- `spammer_android.py` - Script utama (Multi-Line Messages)
- Panduan konfigurasi ADB lengkap
- Dependensi minimum (hanya Python 3.8+ dan ADB)

---

## 🛠️ Perubahan Teknis

- Menggunakan `subprocess.run()` untuk eksekusi ADB yang lebih stabil
- Peningkatan escape karakter otomatis
- Antarmuka pengguna yang lebih interaktif
- Timer persiapan 5 detik sebelum eksekusi

---

## ⚠️ Catatan Penting

1. **Izin USB Debugging** harus diaktifkan di perangkat
2. Aplikasi chat harus dalam fokus sebelum eksekusi
3. Interval minimal yang disarankan: 1 detik untuk menghindari deteksi spam
4. Mendukung unlimited (Multi-Line Messages) dalam satu siklus

---

## 📥 Instalasi

```bash
# Clone repositori
git clone -b multi-line --single-branch https://github.com/fatonyahmadfauzi/Universal-Spam-Chat-Bot-Android-USB-Debugging.git Universal-Spam-Chat-Bot-Android-USB-Debugging_Multi-Line-Messages

cd Universal-Spam-Chat-Bot-Android-USB-Debugging_Multi-Line-Messages

# Install dependensi (opsional)
pip install -r requirements.txt
```

---

## 🐛 Bug yang Diketahui

- Terkadang gagal mendeteksi perangkat pada koneksi USB pertama kali
- Karakter khusus mungkin perlu escape manual

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah **MIT License** - lihat [LICENSE.md]() untuk detail lengkap.
