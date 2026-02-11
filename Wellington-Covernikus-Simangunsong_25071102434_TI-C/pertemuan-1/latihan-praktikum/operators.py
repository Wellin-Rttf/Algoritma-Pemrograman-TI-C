#Arithmetic Operators
x = 10
y = 2.5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)       #Modulus/sisa pembagian
print(x ** y)      #Exponentiation/Pangkat
print(x // y)      #Floor division: hasil pembagian dibulatkan ke bawah

#Assignment Operators
a = 5
a += 2      #sama dengan a = a + 3
print(a)

a %= 2      #sama dengan a = a % 3
print(a)

a ^= 2      #sama dengan a = a ^ 3
print(a)


#The Walrus Operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:     
    print(f"List has {count} elements")


#Comparison Operators
c = 5
d = 2
print(c == d)       #Equal/sama dengan
print(c != d)       #Not equal/tidak sama dengan
print(c > d)        #Lebih dari
print(c < d)        #Kurang dari
print(c >= d)       #Lebih atau sama dengan
print(c <= d)       #Kurang atau sama dengan

#Chaining Comparison Operators
print(1 < c < 10)
print(1 < c and c < 10)


#Logical Operators
print(c > 0 and c < 10)     #and digunakan untuk mengecek apakah kedua statement benar
print(c > 0 or c < 10)      #or digunakan untuk mengecek apakah salah satu statement benar
print(not(c > 0 and c < 10))     #not digunakan untuk membalikkan hasil dari perbandingan di dalamnya


#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)       #bernilai True karena x memiliki objek yg sama dengan z
print(x is y)       #bernilai False karena x memiliki objek yg sama dengan y, bahkan jika isinya sama
print(x == y)       #bernilai True karena is dan == berbeda, di mana perbandingan == mendeteksi bahwa variabel x dan y sama.

print(x is not y)       #is not mengembalikan nilai True jika kedua variabel tidak memiliki objek yg sama


#Membership Operators. used to test if a sequence is presented in an object
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)       #in untuk mengecek apakah banana terdapat dalam list (True)
print("grape" not in fruits)    #not in untuk mengecek apakah grape terdapat dalam list (True)


text = "Hello World"
print("H" in text)          #Operator membership dapat digunakan di strings.
print("hello" in text)
print("z" not in text)


#Bitwise Operators
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0


Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


#Operator Precedence
#Seperti matematika, perhitungan di python juga memiliki urutan yang kurang lebih sama
"""
Urutannya (dimulai dari yang paling dulu):
Tanda kurung ()
Pangkat **
Perkalian, pembagian, floor division, modulus * / // %
Tambah, kurang + -
Bitwise left and right shifts << >>
Bitwise AND &
Bitwise XOR ^
Bitwise OR  |
Comparisons, identity, and membership operators ==  !=  >  >=  <  <=  is  is not  in  not in
Logika NOT not
AND and
OR or
"""

print(100 + 5 * 3)      #contoh