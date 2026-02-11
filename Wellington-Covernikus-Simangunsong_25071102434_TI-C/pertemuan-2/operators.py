# Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


# The Walrus Operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


# Comparison operators 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Logical Operators
x = 5

print(x > 0 and x < 10)         # Bernilai True jika semuanya benar
print(x > 0 or x < 10)          # Bernilai True jika setidaknya salah satunya benar
print(not(x > 3 and x < 10))    # Not sebagai negasi dari suatu poperasi



# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)       # True karena memiliki alamat yang sama
print(x is y)       # False karena memiliki alamat yang sama
print(x == y)       # True karena hanya mengecek apakah isinya kontennya sama

print(x is not y)


# Membership Operators: Untuk mengecek apakah sesuatu terdapat dalam suatu objek
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) 
print("pineapple" not in fruits)


text = "Hello World"
print("H" in text)          
print("hello" in text)      # False karena kode ascii h dan H berbeda
print("z" not in text)      # Perhatikan kode 'not'



# Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010


# Precedence Order
print(100 + 5 * 3)