def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    return sum(nilai) / len(nilai)

data = [80, 75, 90, 60, 85]
print("Rata-rata =", rata_rata(data))