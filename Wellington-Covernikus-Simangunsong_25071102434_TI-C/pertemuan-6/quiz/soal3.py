"""
Soal 3. Perhitungan Denda Keterlambatan
Topik: While Loop, If-Else| Estimasi waktu: 20 menit
Deskripsi:
Setelah data peminjaman diketahui, petugas perlu menghitung total denda jika anggota 
terlambat mengembalikan buku.
Ketentuan Program:
1. Minta pengguna menginput jumlah hari keterlambatan.
2. Gunakan while loop untuk memastikan hari keterlambatan tidak kurang dari 0. Jika < 0, 
tampilkan pesan error dan minta input ulang.
3. Hitung total denda berdasarkan buku yang dipinjam dan hari keterlambatan.
• Gunakan if-else untuk menampilkan pesan:
• "Tidak ada denda" jika hari keterlambatan = 0, atau
• "Total denda Anda: Rp ..." jika ada keterlambatan.
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

while True:
    buku_yang_dipinjam = int(input("Masukkan nomor buku yang dipinjam: "))
    if buku_yang_dipinjam < 1 or buku_yang_dipinjam > 5:
        print("Masukkan nomor yang valid!")
    else:
        if buku_yang_dipinjam == 1:
            denda = list_buku[0][1]
        elif buku_yang_dipinjam == 2:
            denda = list_buku[1][1]
        elif buku_yang_dipinjam == 3:
            denda = list_buku[2][1]
        elif buku_yang_dipinjam == 4:
            denda = list_buku[3][1]
        elif buku_yang_dipinjam == 5:
            denda = list_buku[4][1]
    
        hari_keterlambatan = int(input("Masukkan jumlah hari keterlambatan peminjaman: "))
        if hari_keterlambatan < 0:
            print("Masukkan nomor yang valid!")
        else:
            if hari_keterlambatan == 0:
                print("Tidak ada denda")
            else:
                total_denda = denda * hari_keterlambatan
                print(f"Total denda Anda: Rp{total_denda}")
                break