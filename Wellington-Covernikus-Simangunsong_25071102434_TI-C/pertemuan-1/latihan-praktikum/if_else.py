#Python Conditions and If statements
a = 25
b = 200
if b > a:
  print("b besar dari a")       #ingat indentasi

is_logged_in = True
if is_logged_in:                #boolean dapat digunakan dalam if tanpa operator perbandingan
  print("Welcome back!")


#Elif Keyword: Jika kondisi sebelumnya tidak benar, coba yanng ini.
a = 25
b = 25
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#Kita dapat membuat lebih dari satu elif condition, dan yang dieksekusi adalah yang benar paling dulu
#Elif digunakan ketika kita punya beberapa kondisi untuk dicek, contohnya:
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")


#Else Keyword: Dieksekusi ketika kondisi if (dan elif) bernilai False
x = 100
y = 25
if y > x:
  print("y is greater than x")
elif x == y:
  print("x and y are equal")
else:
  print("x is greater than y")


#Mengkombinasikan If-Elif-Else
#Temperature classifier:
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


#Short Hand If ... Else
#Sintaksnya berpola: variable = value_if_true if condition else value_if_false
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


#Nested If Statements: If di dalam if
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


#The pass Statement: Digunakan ketika ingin tidak mengeksekusi suatu kode pada if
umur = 16

if umur < 18:
  pass # Fitur anti anak di bawah umur ditambahkan nanti
else:
  print("Access granted")

