a = 314    #integer/bilangan bulat dapat berupa bilang positif atau negatif

b = 3.14   #float/bilangan desimal dapat berupa bilang positif atau negatif, satu atau lebih angka di belakang koma

c = 1j     #complex ditulis dengan j sebagai bilangan imajinari

print(type(a))
print(type(b))
print(type(c))


#Tipe data dapat dikonversi
x = float(a)    #int ke float
y = int(b)      #float ke int
z = complex(a)  #int ke complex

print(type(x))
print(type(y))
print(type(z))


#Kita dapat menggunakan modul built-in dalam python untuk membuat nomor acak
import random   #modul random

print(random.randrange(1, 10))