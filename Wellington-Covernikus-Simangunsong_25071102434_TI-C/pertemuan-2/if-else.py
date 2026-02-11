# If
a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")


# if-elif-else chain
temperature = 22

if temperature > 30:
  print("It's hot outside!")        # 
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")



# Short hand if
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")         #Baca dari tengah

a = 10
b = 20
bigger = a if a > b else b                  # Polanya: variable = value_if_true if condition else value_if_false
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")       # 


# Logical Operators
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")



# Nested If Statements: if di dalam if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


# Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


# The Pass Statement: Ketika tidak ingin melakukan apa-apa setelah sebuah kode dieksekusi
a = 33
b = 200

if b > a:
  pass


# Contohnya: Digunakan saat pengembangan
age = 16
if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

score = 85
if score > 90:
  pass # This is excellent
print("Score processed")


# pass with Multiple Conditions
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")


def calculate_discount(price):
  pass # TODO: Implement discount logic
# Fungsinya ada tapi gak ngelakuin apa-apa