import time
import subprocess
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print("""
    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██████╗ 
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
    ███████╗██████╔╝███████║██╔████╔██║█████╗  ██████╔╝
    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗
    ███████║██║     ██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
    Android Text Spam Bot (ADB)
    """)

def check_adb():
    try:
        subprocess.run(['adb', 'devices'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except:
        return False

def send_message(text):
    # Escape karakter khusus
    escaped_msg = (
        text.replace(' ', '%s')
           .replace('"', '\\"')
           .replace("'", "\\'")
           .replace("&", "\\&")
           .replace("(", "\\(")
           .replace(")", "\\)")
    )
    subprocess.run(['adb', 'shell', 'input', 'text', escaped_msg], stderr=subprocess.DEVNULL)
    subprocess.run(['adb', 'shell', 'input', 'keyevent', '66'], stderr=subprocess.DEVNULL)  # Tombol Enter
    time.sleep(0.3)

def main():
    clear_screen()
    show_banner()
    
    # Cek koneksi ADB
    if not check_adb():
        print("\n❌ Error: ADB tidak terdeteksi. Periksa:")
        print("1. USB Debugging aktif di perangkat")
        print("2. ADB terinstall dan ada di PATH")
        print("3. Perangkat terkoneksi dan diizinkan")
        input("\nTekan Enter untuk keluar...")
        return
    
    print("\n📱 Perangkat Android Terkoneksi:")
    subprocess.run(['adb', 'devices'])
    
    # Konfigurasi dasar
    print("\n⚙️ Konfigurasi Dasar")
    count = int(input("Jumlah pengulangan: "))
    gap = float(input("Jeda antar pengulangan (detik): "))
    bot_prompt = input("Tambahkan status bot? (y/n): ").lower() == 'y'
    
    # Konfigurasi pesan teks - TANPA BATAS
    messages = []
    print("\n📝 Konfigurasi Pesan Teks")
    print("Anda bisa menambahkan pesan sebanyak yang diinginkan!")
    print("Ketik 'SELESAI' di baris baru ketika sudah cukup")
    
    msg_count = 0
    while True:
        msg_count += 1
        msg = input(f"Masukkan pesan teks #{msg_count} (atau 'SELESAI' untuk berhenti): ")
        if msg.upper() == 'SELESAI':
            if msg_count == 1:
                print("Anda harus memasukkan minimal 1 pesan!")
                msg_count = 0
                continue
            break
        messages.append(msg)
    
    # Konfirmasi
    clear_screen()
    show_banner()
    print("\n📝 Ringkasan Konfigurasi:")
    print(f"- Jumlah pengulangan: {count}")
    print(f"- Jeda antar pengulangan: {gap} detik")
    print(f"- Jumlah pesan teks per pengulangan: {len(messages)}")
    for i, msg in enumerate(messages, 1):
        print(f"  {i}. {msg[:50]}{'...' if len(msg) > 50 else ''}")
    
    input("\n⚠️ Pastikan aplikasi chat sudah terbuka dan siap! Tekan Enter untuk mulai...")
    print("\n🔄 Memulai dalam 5 detik...")
    time.sleep(5)
    
    # Proses pengiriman
    success_count = 0
    try:
        for cycle in range(1, count+1):
            print(f"\n♻️ Pengulangan {cycle}/{count}")
            
            # Kirim pesan teks
            for i, msg in enumerate(messages, 1):
                final_msg = f"[{cycle}/{count}] {msg}" if bot_prompt else msg
                print(f"  📨 Mengirim pesan {i}/{len(messages)}: {final_msg[:50]}{'...' if len(final_msg) > 50 else ''}")
                send_message(final_msg)
                time.sleep(0.2)  # Jeda lebih cepat antar pesan
            
            success_count += 1
            if cycle < count:
                print(f"\n⏳ Menunggu {gap} detik sebelum pengulangan berikutnya...")
                time.sleep(gap)
    
    except KeyboardInterrupt:
        print("\n⏹️ Proses dihentikan oleh pengguna")
    
    print(f"\n✅ Selesai! Berhasil mengirim {success_count}/{count} pengulangan")
    input("\nTekan Enter untuk keluar...")

if __name__ == "__main__":
    main()