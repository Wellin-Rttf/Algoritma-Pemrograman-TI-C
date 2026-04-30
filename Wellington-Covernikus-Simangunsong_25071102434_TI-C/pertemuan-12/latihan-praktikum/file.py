struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
    },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
        }
    },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder):
    total = 0
    for item, value in folder.items():
        if type(value) is dict:
            total += total_ukuran(value)
        else:
            total += value
    return total

def hitung_file(folder):
    total = 0
    for item, value in folder.items():
        if type(value) is dict:
            total += hitung_file(value)
        else:
            total += 1
    return total

def cari_terbesar(folder):
    terbesar = ("", 0)
    for item, value in folder.items():
        if type(value) is dict:
            kandidat = cari_terbesar(value)
            if kandidat[1] > terbesar[1]:
                terbesar = kandidat
        else:
            if value > terbesar[1]:
                terbesar = (item, value)
    return terbesar

def tampilkan_tree(folder, nama = "root", level = 0):
    indent = "  " * level
    print(f"{indent} 📁 {nama}")
    for item, value in folder.items():
        if type(value) is dict:
            tampilkan_tree(value, item, level + 1)
        else:
            print("  " * (level + 1) + f"📝 {item} ({value} KB)")


print(f"Total ukuran skripsi: {total_ukuran(struktur)} KB")

print(f"\nJumlah file: {hitung_file(struktur)} file")

nama, ukuran = cari_terbesar(struktur)
print(f"\nFile terbesar: {nama} ({ukuran} KB)")

print("\nStruktur folder:")
tampilkan_tree(struktur["Skripsi_Aqil"], "Skripsi_Aqil")
