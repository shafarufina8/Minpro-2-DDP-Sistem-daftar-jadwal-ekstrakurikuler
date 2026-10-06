# Minpro-2-DDP-Sistem-daftar-jadwal-ekstrakurikuler

Nama: Shafa Aurellia Rufina Maharani
NIM: 2609116001

Penjelasan program:

program ini adalah sistem manajemen jadwal ekstrakurikuler menggunakan data dictionary, library os, pwinput,  prettytable, dan time. Saat login juga dapat pecobaan 3 kali dan ada perbedaan akses antara admin dan juga siswa.

-----OUTPUT-----

<img width="437" height="152" alt="login admin" src="https://github.com/user-attachments/assets/db2fb4ab-9a6f-4739-bda6-974e45ebbd35" />

gambar diatas login menggunakan akun admin dengan password yang benar.

<img width="427" height="287" alt="admin" src="https://github.com/user-attachments/assets/666ee5ce-d3a1-4f61-b0e2-3269122596d6" />

setelah login akan menampilkan 5 menu pada akun admin.

<img width="492" height="291" alt="pil 1" src="https://github.com/user-attachments/assets/ad8f7fdf-dc10-4eb8-872d-f76a955ea5d2" />

Hasil ketika memilih pilihan 1.

<img width="425" height="337" alt="pil 2" src="https://github.com/user-attachments/assets/8c2f4d76-994d-4de0-b845-bbbcc7ae764f" />

Pada pilihan kedua untuk menambah ekskul .

<img width="560" height="505" alt="pil 3" src="https://github.com/user-attachments/assets/de381c70-1e5d-426b-ba9a-7574ad59b41d" />

hasil penambahan ekskul dan ini merupakan pilihan 3 yaitu mengubah data yang sudah ada.

<img width="567" height="362" alt="pil 4" src="https://github.com/user-attachments/assets/f1fe32d8-dad9-4936-af9c-aab8ddd044dc" />

ini pilihan 4 untuk menghapus ekskul yang diinginkan.

<img width="606" height="320" alt="pil 5" src="https://github.com/user-attachments/assets/4f20371e-a914-49bb-b21d-87fc24eff0ae" />

akhir dari sistem pada pilihan 5.

<img width="417" height="202" alt="login siswa" src="https://github.com/user-attachments/assets/0c3adf4c-dbb9-470b-bcea-950846196a6a" />

Gambar diatas login sebagai siswa, hanya terdapat 2 pilihan.

<img width="447" height="195" alt="penggunaan value error" src="https://github.com/user-attachments/assets/3ea8cf30-ca0d-4e78-95b1-606537f71087" />

saat memilih pilihan tidak bisa memasukkan huruf, hanya bisa angka.

<img width="492" height="192" alt="login salah" src="https://github.com/user-attachments/assets/da95f6a4-49dc-4c56-b888-238b04df5214" />

login dengan username/password yang salah akan diberi kesempatan 3 kali, jika sudah sampai batas program berhenti.

<img width="1004" height="8084" alt="flowchart mipro 2 drawio" src="https://github.com/user-attachments/assets/222b2942-68f0-4a0d-b057-887225d3dd7a" />

A. Mulai & Login:
Begitu program dibuka, kamu diminta masukin *username* sama *password*. Kamu dikasih kesempatan **3 kali mencoba**. Kalau salah terus, pintu terkunci (program langsung keluar/berhenti).

B. Pengecekan Tipe User (Peran):
Setelah berhasil masuk, sistem bakal ngeliat siapa kamu:
1. Kalau Admin: dikasih akses penuh buat ngelola data (bisa ngeliat jadwal, nambah ekskul baru, ngedit data lama, atau ngehapus ekskul).
2. Kalau Siswa: cuma bisa ngeliat tabel jadwal ekskul aja, tidak bisa ngubah apa-apa.

C. Proses Pengerjaan (Pilihan Menu):
1. Lihat Jadwal: Menampilkan daftar ekskul rapi dalam bentuk tabel. Kalau data masih kosong, nanti ada pemberitahuan.
2. Tambah Ekskul: diminta masukin kode baru (tidak boleh sama seperti yang sudah ada). tinggal isi nama ekskul, hari, dan pembinanya.
3. Ubah Data: ilih kode ekskul yang mau diganti. Data lamanya bakal kelihatan, dan tinggal ketik data barunya (kalau nggak mau diubah, tinggal tekan Enter aja).
4. Hapus Data: masukin kode ekskul yang mau dibuang, lalu sistem bakal nanya konfirmasi "yakin mau hapus?" sebelum beneran dihapus.

D. Selesai
Kalau udah beres, tinggal pilih menu Keluar, dan program selesai berjalan.

