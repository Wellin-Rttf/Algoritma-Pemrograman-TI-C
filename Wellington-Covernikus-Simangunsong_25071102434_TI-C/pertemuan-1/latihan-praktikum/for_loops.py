# Perulangan for digunakan untuk mengulangi suatu urutan,
# baik berupa list, tuple, dictionary, set, atau string.

for x in "teks":     # Loop setiap huruf di string "teks"
  print(x)

kalimat = ["ini", "sebuah", "teks"]
for y in kalimat:
  print(y)
  if y == "sebuah":
    break           # Dengan break kita dapat menghentikan loop sebelum semuanya diulangi

kalimat = ["ini", "sebuah", "teks"]
for z in kalimat:
  if z == "sebuah":
    continue           # Dengan continue kita dapat menghentikan loop pada iterasi "sebuah" dan lanjutkan yang lainnya
  print(z)

# Fungsi range()
for x in range(6):
  print(x)


# Nested Loops: Loop di dalam loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#  Pass juga ada pada else
for x in [0, 1, 2]:
  pass