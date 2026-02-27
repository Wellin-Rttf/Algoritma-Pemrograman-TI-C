# Menggunakan input untuk meminta masukan dari pengguna
name = input("Masukkan nama Anda: ")
print(f"Nama Anda adalah {name}.")


# Mengubah tipe data input
age = int(input("Masukkan umur Anda: "))
print(f"Anda berumur {age} tahun.")


# Menggunakan try exception untuk memastikan bahhwa pengguna memasukkan integer
try:
    finger = int(input("Masukkan jumlah jari kedua tangan Anda: "))
    print(f"Jari kedua tangan Anda ada {finger}.")
    
except ValueError:
    print("Jumlah yang Anda masukkan tidak valid!")