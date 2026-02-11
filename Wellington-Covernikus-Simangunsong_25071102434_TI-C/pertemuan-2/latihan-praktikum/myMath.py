a = 9
b = 3

def penambahan(a, b):
  return a + b

print(penambahan(a, b))


def pengurangan(a, b):
  return a - b
print(pengurangan(a, b))


def perkalian(a, b):
  return a * b
print(perkalian(a, b))


def pembagian(a, b):
  return a / b

if b == 0:
    print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
else:
    print(pembagian(a, b))


def modulus(a, b):
  return a % b
print(modulus(a, b))


def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(5):
    print(fibonacci(i), end=" ")