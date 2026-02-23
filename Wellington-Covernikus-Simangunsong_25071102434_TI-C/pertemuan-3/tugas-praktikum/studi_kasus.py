# Kalkulator sederhana
class Kalkulator:

    def tambah(self, a, b):
        return a + b
    
    def kurang(self, a, b):
        return a - b
    
    def kali(self, a, b):
        return a * b
    
    def bagi(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:    
            print("Tidak bisa membagi angka dengan 0!")
            return None


kalkulator = Kalkulator()

while True:
    try:
        angka1 = float(input("Masukkan bilangan pertama: "))
        operator = input("Masukkan operasi yang digunakan (+, -, *, /): ")
        angka2 = float(input("Masukkan bilangan kedua: "))
        
        if operator == "+":
            print("Hasil: ", kalkulator.tambah(angka1, angka2))
        elif operator == "-":
            print("Hasil: ", kalkulator.kurang(angka1, angka2))
        elif operator == "*":
            print("Hasil: ", kalkulator.kali(angka1, angka2))
        elif operator == "/":
            hasil = kalkulator.bagi(angka1, angka2)
            if hasil != None:
                print("Hasil: ", hasil)
        else:
            print("Operasi tidak valid!")
    
    except ValueError:
        print("Input tidak valid!")
    
    print()
    x = input("Apakah anda ingin melakukan perhitungan lagi? [y/n]\n")
    if x == "n":
        break
