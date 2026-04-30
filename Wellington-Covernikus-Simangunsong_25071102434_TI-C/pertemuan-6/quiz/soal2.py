"""
Soal 2. Menghitung Total Peminjaman
Topik: While Loop, For Loop | Estimasi waktu: 20 menit
Deskripsi:
Berdasarkan Soal 1 kembangan kode agar anggota dapat meminjam lebih dari satu buku dan 
program menghitung estimasi denda.
Ketentuan Program:
1. Gunakan while loop agar anggota dapat terus menambah buku pinjaman. Loop berhenti 
ketika anggota memasukkan angka 0.
2. Simpan setiap buku yang dipinjam ke dalam list berisi judul buku dan lama pinjam (hari).
3. Setelah selesai, tampilkan daftar buku yang dipinjam menggunakan for loop.
4. Hitung total estimasi denda jika semua buku terlambat 1 hari (simulasi sederhana) an 
tampilkan hasilnya..
"""
list_buku = [["Algoritma", 2000],
             ["Basis Data", 2500],
             ["Stuktur Data", 3000],
             ["Arsitektur Komputer", 2500],
             ["Aljabar Linear", 2000]]

nomor = 1
for x, y in list_buku:
    print(f"{nomor}. Buku: {x}. Denda keterlambatan per hari: Rp{y}.")
    nomor += 1

print()

list_dipinjam = []
i = 1
while i != 0:
    pilihan = int(input("Masukkan nomor buku yang ingin kamu pinjam (Ketik 0 jika selesai): "))
    if pilihan == 1:
        lama = int(input("Masukkan lama hari peminjaman: "))
        list_dipinjam.append([list_buku[0][0], lama])
    elif pilihan == 2:
        lama = int(input("Masukkan lama hari peminjaman: "))
        list_dipinjam.append([list_buku[1][0], lama])
    elif pilihan == 3:
        lama = int(input("Masukkan lama hari peminjaman: "))
        list_dipinjam.append([list_buku[2][0], lama])
    elif pilihan == 4:
        lama = int(input("Masukkan lama hari peminjaman: "))
        list_dipinjam.append([list_buku[3][0], lama])
    elif pilihan == 5:
        lama = int(input("Masukkan lama hari peminjaman: "))
        list_dipinjam.append([list_buku[4][0], lama])
    elif pilihan == 0:
        break    
    else:
        print("Pilihan buku yang anda pilih tidak valid!")
    
nomor = 1
print(f"Daftar buku yang dipinjam:")
for x, y in list_dipinjam:
    print(f"{nomor}. Buku yang dipinjam: {x}. Lama hari peminjaman: {y}.")
    nomor += 1