# The Python Match Statement: Alih-alih mengetik banyak statement if..else, kita dapat menggunakan statement match
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# Gunakan underscore _ ketika ingin mengeksekusi suatu kode terakhir jika tidak ada kode lain yang sesuai
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


#Mengkombinasikan value menggunakan karakter pipa | untuk mengecek lebih dari satu value dalam satu case
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")