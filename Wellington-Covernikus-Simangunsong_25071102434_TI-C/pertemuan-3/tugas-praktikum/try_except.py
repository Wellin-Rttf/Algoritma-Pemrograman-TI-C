# Contoh kode try dan except pada pembagian dengan penyebut nol
try:
    x = 3 / 0
    print(x)
except:
    print("An exception occurred.")


# Beberapa exception dalam try except
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Else jika tidak terjadi kesalahan dalam kode try
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# Finally akan selalu dieksekusi setelah try dan except
try: 
    y = 5 // 0
    print(y) 

except ZeroDivisionError:    
    print("Can't divide by zero") 

finally: 
    print("This is always executed")


# Memunculkan except dengan raise
x = "hello"

if type(x) is not int:
  raise TypeError("Only integers are allowed")
