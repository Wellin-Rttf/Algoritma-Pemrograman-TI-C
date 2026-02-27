matrix = [[0, 1, 2],
          [0, 1, 0],
          [3, 4, 5]]

print(matrix)
print(matrix[0][2])


# list comprehension
M = 2
N = 3
matrix2 = [[0 for j in range(M)] for i in range (N)]
print(matrix2)


# Transpose matriks: membalik dimensi
# print((zip(*matrix)))

# Determinan: selisih dari diagonal utama dengan diagonal sekunder
