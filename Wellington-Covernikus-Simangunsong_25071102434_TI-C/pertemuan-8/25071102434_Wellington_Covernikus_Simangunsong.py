# ===== BAGIAN A =====
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

riwayat = []

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    # Menentukan pemenang dengan menggunakan if-else dan mengembalikan nilai pemenang
    if (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "pemain"
    elif pilihan_pemain == pilihan_komputer:
        return "seri"
    else:
        return "komputer"

def main_satu_giliran(nomor_giliran):
    # Rumus untuk pilihan komputer
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:     # Perulangan while digunakan agar input dan outut dapat diulang
        pilihan_pemain = input("Masukkan pilihan kamu (batu, gunting, kertas): ")

        if pilihan_pemain not in DAFTAR_PILIHAN:
            print("Masukkan pilihan yang valid!")
        hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
        if hasil == "pemain" or hasil == "komputer":
            print("===============")
            print(f"{hasil} menang")
            print("===============")
            print(f"Komputer: {pilihan_komputer}")
            print(f"Pemain: {pilihan_pemain}")
        else:
            print(f"Hasilnya {hasil}")
        return hasil

def main_satu_ronde(nama, nomor_ronde):
    # Deklarasi nomor giliran, jumlah kemenangan komputer dan pemain
    nomor_giliran = 0
    komputer_menang = 0
    pemain_menang = 0
    
    # selama komputer atau pemain belum menang lebih dari 3 kali dalam satu ronde, permainan akan dijalankan
    while komputer_menang < 3 and pemain_menang < 3:
        hasil = main_satu_giliran(nomor_giliran)
        nomor_giliran += 1      # nomor giliran ditambahkan
        if hasil == "pemain":
            pemain_menang += 1  # jumlah kemenangan pemain ditambah jika hasilnya pemain yang menang
        elif hasil == "komputer":
            komputer_menang += 1    # jumlah kemenangan komputer ditambah jika hasilnya komputer yang menang
    skor = pemain_menang * 10   # Skor diberikan pada yang menang, dengan nilai 10
    return [nama, skor]

main_satu_ronde("Insert Nama", 1)

# ===== BAGIAN B =====
def tampilkan_riwayat(riwayat):
    print("----- + ---------- + ----------")
    #print(f"{nomor_giliran} | {nama < 10} " | {skor < 10})


# ===== BAGIAN C =====
def bubble_sort_riwayat(riwayat):
    salinan = riwayat.copy()
    n = len(salinan)
    for i in range(n-1):
        for j in range(n-i-1):
            if salinan[j] > salinan[j+1]:
                salinan[j], salinan[j+1] = salinan[j+1], salinan[j]
    return salinan

def tampilkan_leaderboard(riwayat):
    bubble_sort_riwayat(riwayat)
    pass


def program_utama():
    nama = input("Masukkan nama kamu: ")
    main_satu_ronde(nama, 1)
    lanjut = input("Kamu mau lanjut lagi? (y/n): ")
    if lanjut == "y":
        while True:
            pass
    if lanjut == "n":
        tampilkan_riwayat(riwayat)
        tampilkan_leaderboard(riwayat)