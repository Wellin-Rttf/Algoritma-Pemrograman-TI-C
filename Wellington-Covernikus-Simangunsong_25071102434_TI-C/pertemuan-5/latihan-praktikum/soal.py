"""
Diberikan dua matriks:
A = [[5, 3, 1],
[2, 8, 4],
[6, 0, 7]]
B = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
Buatlah program python (tanpa NumPy) yang:
a Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah 
b Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
c Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam 
C_skalar
d Hitunglah deteminan matriks A dan B menggunakan Metode Sarrus
e Menampilkan keempat hasil dengan format rapi baris per baris
"""

A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# a
def Penjumlahan(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

c_tambah = Penjumlahan(A, B)

# b 
def Pengurangan(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

c_kurang = Pengurangan(A, B)

# c 
def kali_skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

c_skalar = kali_skalar(A, 4)

# d 
def determinan_3x3(M):
    d1 = M[0][0] * M[1][1] * M[2][2]
    d2 = M[0][1] * M[1][2] * M[2][0]
    d3 = M[0][2] * M[1][0] * M[2][1]

    d4 = M[0][2] * M[1][1] * M[2][0]
    d5 = M[0][0] * M[1][2] * M[2][1]
    d6 = M[0][1] * M[1][0] * M[2][2]
    return (d1 + d2 + d3) - (d4 + d5 + d6)

# e  
print("Diketahui matriks A:")
for baris in A:
    print(baris)

print("\nDiketahui matriks B:")
for baris in B:
    print(baris)

print("\nHasil dari penjumlahan matriks A dan B adalah:")
for baris in c_tambah:
    print(baris)

print("\nHasil dari pengurangan matriks A dan B adalah:")
for baris in c_kurang:
    print(baris)

print("\nHasil dari perkalian matriks A dengan skalar k = 4 adalah:")
for baris in c_skalar:
    print(baris)

print(f"\nHasil dari determinan matris A adalah {determinan_3x3(A)}")
print(f"Hasil dari determinan matris B adalah {determinan_3x3(B)}")

