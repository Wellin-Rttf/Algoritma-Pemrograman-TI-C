#Untuk mengetahui sebuah ekspresi True atau False, kita menggunakan boolean

print(10 > 5)
print(10 == 5)
print(10 < 5)

a = 200
b = 25

if b > a:
  print("b lebih besar dari a")
else:
  print("b lebih kecil dari a")

#Semua string, list, tuple, set, dictionary bernilai True selama string-nya tidak kosong
#Semua angka bernilai True selain angka 0
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(""))        #bernilai False

#Function can Return A Boolean
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")