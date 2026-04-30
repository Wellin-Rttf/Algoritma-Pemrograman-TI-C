"""
Buat program untuk menampilkan daftar buku yang tersedia dan meminta anggota memilih 
satu buku.
Ketentuan Program:
1. Buat list buku berisi 5 item buku beserta denda per hari keterlambatan, contoh: 
[["Algoritma", 2000], ["Basis Data", 2500], ...].
2. Tampilkan seluruh daftar buku beserta denda menggunakan for loop dengan penomoran.
3. Minta pengguna memasukkan nomor buku yang dipilih.
4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan error; 
jika valid, tampilkan judul buku dan denda per hari.
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

pilihan = int(input("Masukkan nomor buku yang ingin dipilih: "))
if pilihan == 1:
    print(f"Buku yang dipilih: {list_buku[0][0]}")
    print(f"Denda keterlambatan per hari: Rp{list_buku[0][1]}")
elif pilihan == 2:
    print(f"Buku yang dipilih: {list_buku[1][0]}")
    print(f"Denda keterlambatan per hari: Rp{list_buku[1][1]}")
elif pilihan == 3:
    print(f"Buku yang dipilih: {list_buku[2][0]}")
    print(f"Denda keterlambatan per hari: Rp{list_buku[2][1]}")
elif pilihan == 4:
    print(f"Buku yang dipilih: {list_buku[3][0]}")
    print(f"Denda keterlambatan per hari: Rp{list_buku[3][1]}")
elif pilihan == 5:
    print(f"Buku yang dipilih: {list_buku[4][0]}")
    print(f"Denda keterlambatan per hari: Rp{list_buku[4][1]}")
else:
    print("Pilihan buku yang anda pilih tidak valid!")