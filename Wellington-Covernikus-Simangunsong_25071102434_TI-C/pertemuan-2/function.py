def myFunction(world = "world"):
    print("Hello", world)

myFunction()


# Return values
def get_greeting():
  return "Hello from a function"        # Fungsi ini mengembalikan string

message = get_greeting()                # Fungsi dipangil lalu disimpan ke variabel message
print(message)

print(get_greeting())                   # Atau bisa dipanggil langsung



# Python Scope
# Local scope
def myfunc():
  x = 300
  print(x)

myfunc()


# Global scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)


# Lambda function: Fungsi anonimus yang hanya dapat dieksekusi sekali
x = lambda a : a + 10
print(x(5))


#Recursion function: Ketika sebuah fungsi memanggil dirinya sendiri
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)


# Base case and Recursive Case
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))



