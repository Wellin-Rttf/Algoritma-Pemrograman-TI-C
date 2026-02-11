a = 2
b = "Dua"
print(a)
print(b)    #Python tidak mempunyai command untuk mendeklarasikan tipe data seperti bahasa C
#Tetapi jika ingin membuat tipe data spesifik dapat melakukan casting
d = str(3.14)   #Akan dibaca sebagai string
e = int(3.14)   #Akan dibaca sebagai 3 saja
f = float(3) #Akan dibaca sebagai 3.0
print(d)
print(e)
print(f)

#Kita dapat mengecek tipe data sebuah variabel dengan type()
print(type(d))
print(type(e))
print(type(f))

#Nama variabel sensitif terhadap huruf kecil atau besar
g = 1
G = "Satu"
print(g)
print(G)

#Nama variabel harus diawali huruf atau underscore
#Tidak boleh diawali angka
#Hanya boleh mengandung huruf, angka, dan underscore
_contoh_Variabel = "Teks"
contoh_Variabel = "Teks"
contohVariabel3 = "Teks"

iniNamaVariabel = "Hello world!"   #Contoh variable name bergaya Camel Case
IniNamaVariabel = "Hello world!"   #Contoh variable name bergaya Pascal Case
ini_nama_variabel = "Hello world!"   #Contoh variable name bergaya Snake Case

#Kita dapat meng-assign beberapa value ke variabel dalam satu baris
x, y, z = "Ini", "Teks", "Saya"
print(x)
print(y)
print(z)

#Atau meng-assign satu value ke beberapa variabel 
x = y = z = "Ini Teks Saya"
print(x)
print(y)
print(z)

#Kita dapat menampilkan output beberapa variabel menggunakan koma
x = "Halo"
y = "yang"
z = "di sana"
print(x, y, z)

x = "Halo "
y = "yang "
z = "di sana"
print(x + y + z)    #Atau memakai operator tambah, bedanya harus memakai spasi pada string agar dapat dibaca

#Global variables
h = "awesome"

def myfunc():
  global h
  h = "fantastic"           #Alih-alih awesome, fantastic akan digunakan seterusnya
  print("Python is " + x)

myfunc()

print("Python is " + x)
