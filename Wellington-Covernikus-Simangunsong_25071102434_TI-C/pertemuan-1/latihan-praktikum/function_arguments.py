# Informasi dapat dikirim ke fungsi sebagai argumen, ditulis dalam tanda kurung setelah nama fungsi, dan dipisahkan koma.

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameter vs Argument
# Parameter adalah variabel dalam definisi fungsi
# Argument adalah nilai nyata yang dikirim saat fungsi dipanggil
def greet(name):  # name adalah parameter
    print("Hello", name)
greet("Emil")  # Emil adalah argument


# Jumlah argumen harus sesuai
def full_name(fname, lname):
    print(fname + " " + lname)

full_name("Emil", "Refsnes")


# Default parameter values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# Keyword arguments (kwargs)
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")  # urutan tidak masalah


# Positional arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
# urutan penting dalam positional argument


# Campuran positional dan keyword arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# Mengirim berbagai tipe data
# Misalnya mengirim list sebagai argumen:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


# Return values
# Fungsi dapat mengembalikan nilai dengan menggunakan pernyataan return:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


# Fungsi dapat mengembalikan tipe data apa saja seperti list, tuple, dictionari, dll.
# Return list
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Return tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)


# Positional-only arguments (gunakan /)
def my_function(name, /):
  print("Hello", name)

my_function("Emil")


# Keyword-only arguments (gunakan tanda *)
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")


# Kombinasi positional-only dan keyword-only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)