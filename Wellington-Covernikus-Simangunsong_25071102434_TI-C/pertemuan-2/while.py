# 
i = 1
while i < 6:
  print(i)
  i += 1

# break dan continue: break artinya berhenti, continue artinya dilewati
i = 1
while i < 6:
  print(i)
  if i == 3:            # akan berhenti ketika i sampai di 3
    break
  i += 1


i = 0
while i < 6:
  i += 1
  if i == 3:            # 3 akan dilewati
    continue
  print(i)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")