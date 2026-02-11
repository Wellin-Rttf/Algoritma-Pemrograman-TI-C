#Kita dapat menggunakan tanda petik satu atau petik dua dalam strings

#Kita juga dapat menggunakan kutipan dalam string
print("It's alright")
print("He is called 'John'")
print('He is called "John"')

#Meng-assign string ke sebuah variabel
a = "Hello"
print(a)

#Kita dapat membuat string dengan beberapa baris dengan 3 tanda petik
b = """Contoh teks
dalam 
beberapa baris"""       #atau tiga tanda etik satu
print(b)

#String dalam python adalah array
c = ("Teks")
print(c[0])     #Karakter pertama dimulai dengan indeks 0, sehingga kode ini akan menampilkan T

#Loop pada string
for x in "teks":
  print(x)

#Mencari panjang string
x = "Teks"
print(len(x))

#Mencari teks pada sebuah string
print("baris" in b) #menampilkan true or false

#Slicing:  menampilkan potongan teks tertentu
d = "Hello, World!"
print(d[2:5])       #menampilkan teks dari indeks 2 ke 5 (tidak termasuk yg akhir), indeks dimulai dari 0
print(d[:5])        #potong dengan range dari indeks awal ke indeks 5
print(d[2:])        #potong dengan range dari indeks 5 ke indeks akhir
print(d[-5:-2])     #slice teks dari belakang


#Memodifikasi string
d = " Hello, World! "
print(d.upper())    #mengubah menjadi huruf kapital
print(d.lower())    #mengubah menjadi huruf kecil
print(d.strip())    #menghapus spasi dari sebelum dan sesudah teks

print(d.replace("H", "K"))  #mengganti teks
print(d.split(","))         #memisahkan teks jika terdapat pemisah yang dimaksud

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b        #Menggabungkan teks
print(c)

#String Format
#F-Strings
age = 22
txt = f"Saya berumur {age}"     #Kurung kurawal sebagai placeholder
print(txt)

#Placeholders and Modifiers
price = 12
txt = f"The price is {price:.2f} dollars"       #Placeholder dapat mengandung variabel, operasi, fungsi, dan modifier
print(txt)

#Escape Characters
x = "Contoh teks yang berisi \"kutipan\"."  #Kita dapat memakai \ sebelum karakter yang tidak dapat dituliskan dalam sebuah string
print(x)