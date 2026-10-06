import os
import time
from prettytable import PrettyTable
import pwinput

Daftar_ekskul = {
    "EKS1": {"Nama": "Basket", "Hari": "Rabu", "Pembina": "Pak Rudi"},
    "EKS2": {"Nama": "Badminton", "Hari": "Sabtu", "Pembina": "Pak Dayat"}
}

Users = {
    "admin": {
        "Username": "admin.sekolah",
        "Password": "admin2026", 
        "Role": "admin"
    },
    "siswa": {
        "Username": "siswa.sekolah",
        "Password": "siswa456", 
        "Role": "siswa"
    }
}

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def lihat_ekskul():
    bersihkan_layar()
    print("-" * 40)
    print("     JADWAL EKSTRAKURIKULER")
    print("-" * 40)

    if not Daftar_ekskul:
        print("\n Belum ada data ekstrakurikuler yang terdaftar!")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["Kode", "Nama", "Hari", "Pembina"]
        for kode, detail in Daftar_ekskul.items():
            tabel.add_row([kode, detail["Nama"], detail["Hari"], detail["Pembina"]])
        print(tabel)
    print("-" * 40)

def tambah_ekskul():
    lihat_ekskul()
    print("\n ---TAMBAH EKSKTRAKURIKULER BARU---")

    while True:
        kode = input("Masukkan kode ekskul Baru: ").strip().upper()
        if not kode:
            print("Kode tidak boleh kosong!")
            continue
        if kode in Daftar_ekskul:
            print("Kode ekskul sudah ada, silahkan gunakan kode lain!")
            continue
        break

    nama = input("Masukkan nama ekskul: ").strip()
    hari = input("Masukkan hari ekskul: ").strip()
    pembina = input("Masukkan nama pembina: ").strip()

    if nama and hari and pembina:
        Daftar_ekskul[kode] = {
            "Nama": nama,
            "Hari": hari,
            "Pembina": pembina
        }
        print(f"\nData ekskul berhasil ditambahkan!")
    else:
        print("\nGagal: semua input harus diisi!")

    time.sleep(2)

def ubah_ekskul():
    lihat_ekskul()
    if not Daftar_ekskul:
        input("\nTekan enter untuk kembali...:")
        return

    print("\n---UBAH DATA EKSTRAKURIKULER---")
    kode = input("Masukkan kode ekskul yang ingin diubah: ").strip().upper()

    if kode in Daftar_ekskul:
        print(f"\n[Data lama] Nama: {Daftar_ekskul[kode]['Nama']} \n Hari: {Daftar_ekskul[kode]['Hari']} \n Pembina: {Daftar_ekskul[kode]['Pembina']}")
        print("Masukkan data baru (Tekan enter untuk tidak mengubah):")

        nama_baru = input(f"Nama baru [{Daftar_ekskul[kode]['Nama']}]: ").strip()
        hari_baru = input(f"Hari baru [{Daftar_ekskul[kode]['Hari']}]: ").strip()
        pembina_baru = input(f"Pembina baru [{Daftar_ekskul[kode]['Pembina']}]: ").strip()

        if nama_baru:
            Daftar_ekskul[kode]['Nama'] = nama_baru
        if hari_baru:
            Daftar_ekskul[kode]['Hari'] = hari_baru
        if pembina_baru:
            Daftar_ekskul[kode]['Pembina'] = pembina_baru

        print("\nData ekskul berhasil diperbarui!")
    else:
        print("\nKode ekskul tidak ditemukan!")

    time.sleep(2)

def hapus_ekskul():
    lihat_ekskul()
    if not Daftar_ekskul:
        input("\nTekan enter untuk kembali...:")
        return

    print("\n---HAPUS DATA EKSTRAKURIKULER---")
    kode = input("Masukkan kode ekskul yang ingin dihapus:").strip().upper()

    if kode in Daftar_ekskul:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus '{Daftar_ekskul[kode]['Nama']}'? (y/n): ").strip().lower()
        if konfirmasi == "y":
            data_dihapus = Daftar_ekskul.pop(kode)
            print(f"\nEkskul {data_dihapus['Nama']} berhasil dihapus!")
        else:
            print("\nPenghapusan dibatalkan.")
    else:
        print("\nKode ekskul tidak ditemukan!")

    time.sleep(2)

def login():
    bersihkan_layar()
    print("-" * 40)
    print("    LOGIN MANAJEMEN EKSKTRAKURIKULER")
    print("-" * 40)

    percobaan = 0
    max_percobaan = 3

    while percobaan < max_percobaan:
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password: ", "*").strip()

        if username in Users and Users[username]["Password"] == password:
            print(f"\nLogin berhasil! Selamat Datang, {username}.")
            time.sleep(1)
            return Users[username]
        else:
            percobaan += 1
            sisa = max_percobaan - percobaan
            print(f"Username atau Password salah.sisa percobaan: {sisa}\n")

    print("Anda telah melebihi batas percobaan login. Program berhenti.")
    exit()

def main():
    user_aktif = login()
    role = user_aktif['Role'].lower()

    while True:
        bersihkan_layar()
        print("-" * 40)
        print("  MANAJEMEN EKSTRAKRIKULER")
        print(f"User: {user_aktif['Username']} | Role: {user_aktif['Role'].upper()}")
        print("-" * 40)

#-----------------------
# MENU UNTUK ADMIN
#-----------------------
        if user_aktif['Role'] == 'admin':
            print("1. Lihat jadwal ekskul")
            print("2. Tambah Ekskul Baru")
            print("3. Ubah Data Ekskul")
            print("4. Hapus Ekskul")
            print("5. Keluar")
            print("-" * 40)

            try:
                pilihan = int(input("Masukkan pilihan menu (1-5): "))

                if pilihan == 1:
                    lihat_ekskul()
                    input("\nTekan enter untuk kembali ke menu utama...:")

                elif pilihan == 2:
                    tambah_ekskul()

                elif pilihan == 3:
                    ubah_ekskul()

                elif pilihan == 4:
                    hapus_ekskul()

                elif pilihan == 5:
                    print("\nTerima kasih telah menggunakan sistem ini.")
                    time.sleep(1)
                    break
                
                else:
                    print("\nPilihan menu tidak tersedia (Gunakan angka 1-5).")
                    time.sleep(1)

            except ValueError:
                print("\nInput tidak valid! Harap masukkan angka.")
                time.sleep(1)

#-------------------
# MENU UNTUK SISWA
#-------------------
        else:
            print("1. Lihat jadwal ekskul")
            print("2. Keluar")
            print("-" * 40)

            try:
                pilihan = int(input("Masukkan pilihan menu (1-2): "))
                if pilihan == 1:
                    lihat_ekskul()
                    input("\nTekan enter untuk kembali...")

                elif pilihan == 2:
                    print("\nTerimkasih telah menggunakan sistem ini.")
                    time.sleep(1)
                    break

                else:
                    print("\nPilihan tidak valid! (Pilih 1-2)")
                    time.sleep(1)

            except ValueError:
                print("\nInput tidak valid! Harap masukkan angka.")
                time.sleep(1)

if __name__ == "__main__":
    main()