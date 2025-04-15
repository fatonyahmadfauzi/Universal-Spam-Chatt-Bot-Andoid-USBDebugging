# Universal Spam Chat Bot (Android USB Debugging)

Bot otomatis untuk mengirim pesan berulang di aplikasi chat Android menggunakan ADB via USB Debugging.

![Demo](https://img.shields.io/badge/Platform-Android-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 🔧 Prasyarat

1. **Perangkat Android** dengan USB Debugging aktif
2. **Python 3.8+** terinstal
3. **ADB (Android Debug Bridge)** terkonfigurasi
4. Kabel USB yang mendukung transfer data

## 🚀 Cara Penggunaan

1. Sambungkan Android ke PC via USB
2. Aktifkan **USB Debugging**:
   - Buka _Settings_ > _About Phone_ > Ketuk **Build Number** 7x
   - Kembali ke _Settings_ > _Developer Options_ > Aktifkan **USB Debugging**
3. Jalankan bot:
   ```bash
   python spammer.py
   ```

## ⚙️ Konfigurasi

Edit parameter di script:

```python
msg = "Pesan Anda"  # Pesan yang akan dikirim
count = 10          # Jumlah pengulangan
gap = 1.5           # Interval antar pesan (detik)
```

## 📌 Troubleshooting

| **Error**           | **Solusi**                                     |
| ------------------- | ---------------------------------------------- |
| `adb: no devices`   | Periksa koneksi USB dan aktifkan USB Debugging |
| `Permission denied` | Berikan izin USB Debugging di perangkat        |
| `Command not found` | Pastikan ADB terinstal dan PATH sudah benar    |

## ⚠️ Peringatan

- Gunakan dengan bijak! Spam berlebihan dapat menyebabkan akun diblokir.
- Proyek ini hanya untuk tujuan edukasi.

## 📝 Lisensi

MIT License - Free untuk penggunaan pribadi dan komersial

### 🛠️ **Struktur Proyek Direkomendasikan**

```bash
Universal-Spam-Chatt-Bot-Andoid-USBDebugging/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── spammer_android.py
```
