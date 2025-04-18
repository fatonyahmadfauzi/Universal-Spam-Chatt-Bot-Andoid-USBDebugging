# Release Notes - Universal Spam Chat Bot (Android USB Debugging)

**🚀 Versi 1.0.0 (Stable Release)**
**📅 Release Date**: 2025-04-16

---

## ✨ Fitur Utama

- **Pengiriman Pesan Otomatis** via ADB dengan kontrol penuh atas:
  - Konten pesan
  - Jumlah pengulangan
  - Interval waktu antar pesan
- **Dukungan Multi-Platform**:
  - Windows/macOS/Linux
  - Android 5.0+ (dengan USB Debugging)
- **Sistem Notifikasi Bot** opsional untuk melacak pengiriman

---

## 📦 Komponen

- `spammer_android.py` - Script utama
- Panduan konfigurasi ADB lengkap
- Dependensi minimum (hanya Python 3.8+ dan ADB)

---

## 🛠️ Perubahan Teknis

- Menggunakan `subprocess.run()` untuk eksekusi ADB yang lebih stabil
- Penanganan spasi otomatis dalam pesan
- Timer persiapan 5 detik sebelum eksekusi

---

## ⚠️ Catatan Penting

1. **Izin USB Debugging** harus diaktifkan di perangkat
2. Aplikasi chat harus dalam fokus sebelum eksekusi
3. Interval minimal yang disarankan: 1.5 detik untuk menghindari deteksi spam

---

## 📥 Instalasi

```bash
# Clone repositori
git clone https://github.com/[username]/Universal-Spam-Chat-Bot-Android-USB-Debugging.git
cd Universal-Spam-Chat-Bot-Android-USB-Debugging

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
