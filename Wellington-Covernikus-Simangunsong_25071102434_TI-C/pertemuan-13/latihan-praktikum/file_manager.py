import os

def list_file():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if not files:
        print("Tidak ada file .txt ditemukan")
        return []
    
    print("File tersedia:")
    for i, file in enumerate(files, 1):
        print(f"[{i}] {file}")
    return files

def read_file():
    files = list_file()
    if files:
        try:
            nomor = int(input("Pilih file (nomor): "))
            nama_file = files[nomor-1]
            print(f"--- Isi {nama_file} ---")
            print(open(nama_file, "r").read())
            print("--------------------")
        except:
            print("Input tidak valid!")

def write_file():
    files = list_file()
    tujuan = input("Pilih nomor file atau ketik nama file baru: ")
    
    if tujuan.isdigit() and int(tujuan) <= len(files):
        nama_file = files[int(tujuan)-1]
    else:
        nama_file = tujuan
        
    isi = input("Masukkan isi teks: ")
    with open(nama_file, "w") as f:
        f.write(isi)
    print("File berhasil disimpan!")

def delete_file():
    files = list_file()
    if files:
        try:
            nomor = int(input("Pilih file (nomor): "))
            nama_file = files[nomor-1]
            konfirmasi = input(f"Yakin hapus {nama_file}? (y/n): ")
            if konfirmasi.lower() == "y":
                os.remove(nama_file)
                print("File terhapus")
        except:
            print("Gagal menghapus file")

while True:
    print("""\n============================
PYTHON FILE MANAGER v1.0
============================
[1] Read file
[2] Write file
[3] Delete file
[0] Exit
------------------------------""")
    pilihan = input("Pilih menu: ")
    print()
    if pilihan == "1":
        read_file()
    elif pilihan == "2":
        write_file()
    elif pilihan == "3":
        delete_file()
    elif pilihan == "0":
        break
    else:
        print("Menu tidak valid!")