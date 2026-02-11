# While loop akan mengeksekusi sebuah statement selama sebuah kondisi terpenuhi

i = 1
while i < 6:        # Selama i kurang dari 6,
  print(i)          # print i
  i += 1

# Dengan break Statement kita dapat menghentikan loop bahkan jika kondisi while terpenuhi
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# Dengan statement continue kita dapat berhenti pada iterasi sekarang dan melanjutkan yang lainnya
j = 0
while j < 6:
  j += 1
  if j == 3:
    continue          # 3 akan dilewati
  print(j)


# Dengan statement else kita dapat menjalankan sebuah blok kode ketika kondisinya tidak lagi terpenuhi
k = 1
while k < 6:
  print(k)
  k += 1
else:
  print("k tidak lagi kurang dari 6")
# Blok else tidak akan dijalankan jika loopdihentikan oleh statement break