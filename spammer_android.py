# Script Python yang Dimodifikasi (spammer_android.py)
import time
import subprocess

print("""
📌 Persyaratan:
1. Aktifkan USB Debugging:
   - Buka Pengaturan > Tentang Telepon > Ketuk 'Nomor Build' 7x
   - Kembali ke Pengaturan > Opsi Pengembang > Aktifkan 'USB Debugging'
   
2. Install ADB di komputer:
   - Unduh Platform Tools: https://developer.android.com/studio/releases/platform-tools
   - Ekstrak dan tambahkan path folder ke Environment Variables

3. Sambungkan Android ke PC via USB
4. Pilih 'File Transfer/Android Auto' di notifikasi USB
5. Izinkan koneksi USB Debugging saat muncul popup di HP
""")

input("Tekan Enter setelah semua persiapan selesai...")

print("\n🔄 Pastikan Anda sudah membuka aplikasi chat dan fokus di kolom input!")
print("Waktu persiapan 5 detik dimulai...")
time.sleep(5)

# Input Parameter
msg = input('Pesan yang ingin di-spam: ')
count = int(input('Jumlah pengulangan: '))
gap = float(input('Interval detik antar pesan: '))
bot_prompt = input('Tambahkan status bot? (Y/N): ').upper()

# Proses pengiriman
for i in range(count):
    final_msg = f"[{i+1}/{count}] {msg}" if bot_prompt == 'Y' else msg
    escaped_msg = final_msg.replace(' ', '%s')  # Escape spasi untuk ADB
    subprocess.run(['adb', 'shell', 'input', 'text', escaped_msg])
    subprocess.run(['adb', 'shell', 'input', 'keyevent', '66'])  # Tombol Enter
    time.sleep(gap)

print("\n✅ Semua pesan berhasil dikirim!")