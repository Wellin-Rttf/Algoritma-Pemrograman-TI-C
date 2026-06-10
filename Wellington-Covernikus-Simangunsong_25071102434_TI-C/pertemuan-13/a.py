import os

def read_file():
    print("""File tersedia:
[1] catatan.txt
[2] tugas.txt
[3] jadwal.txt""")
    pilih_file = input("Pilih file (nomor): ")
    if pilih_file == "1":
        f = open("catatan.txt")
        print(f.read())
        print()
    elif pilih_file == "2":
        f = open("tugas.txt")
        print(f.read())
        print()
    elif pilih_file == "3":
        f = open("jadwal.txt")
        print(f.read())
        print()
    else:
        print("Pilih nomor yg tersedia!")


def write_file_ax(file, aorx, user_text):
    if aorx == "append":
        with open(file, "a") as f:
            f.write(user_text)
    elif aorx == "rewrite":
        with open(file, "x") as f:
            f.write(user_text)

def write_file():
    print("""File tersedia:
[1] catatan.txt
[2] tugas.txt
[3] jadwal.txt""")
    nama_file = input("Ketik nomor file yang telah ada atau ketik nama file baru: ")
    if nama_file == "1":
        aorx = input("Kamu ingin menambahkan teks atau menulis ulang file? (ketik append or rewrite) ").lower
        user_text = input("Ketik teks: ")
        write_file_ax("catatan.txt", aorx, user_text)
    elif nama_file == "2":
        aorx = input("Kamu ingin menambahkan teks atau menulis ulang file? (ketik append or rewrite) ").lower
        user_text = input("Ketik teks: ")
        write_file_ax("tugas.txt", aorx, user_text)
    elif nama_file == "3":
        aorx = input("Kamu ingin menambahkan teks atau menulis ulang file? (ketik append or rewrite) ").lower
        user_text = input("Ketik teks: ")
        write_file_ax("jadwal.txt", aorx, user_text)
    else:
        f = open(nama_file, "x")
        with open(nama_file, "a") as f:
            f.write(input("Ketik teks: "))

def delete_file():
    print("""File tersedia:
[1] catatan.txt
[2] tugas.txt
[3] jadwal.txt""")
    pilih_file = input("Pilih file (nomor): ")
    konfirmasi = input("Apakah kamu yakin ingin menghapus (y/n)? ")
    if konfirmasi == "y":
        os.remove(pilih_file)
    else:
        pass


while True:
    print("""\n\n============================
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
