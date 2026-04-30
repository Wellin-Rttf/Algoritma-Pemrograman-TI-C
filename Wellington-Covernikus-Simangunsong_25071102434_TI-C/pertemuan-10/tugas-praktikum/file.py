data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]


def radix_sort(arr):
    array = arr.copy()
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(array)
    exp = 1

    while maxVal // exp > 0:

        while len(array) > 0:
            val = array.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                array.append(val)

        exp *= 10

    return array

print("===== Radix Sort =====")
print(f"Data sebelum diurutkan:\n {data}")
print(f"Data setelah diurutkan: \n{radix_sort(data)}\n\n")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print("===== Merge Sort =====")
print(f"Data sebelum diurutkan:\n {data}")
print(f"Data setelah diurutkan: \n{merge_sort(data)}\n\n")


def linear_search(arr, dicari):
    for i in range(len(arr)):
        if arr[i] == dicari:
            return i, arr[i]
    return -1

print("===== Linear Search =====")
print(f"Data:\n {data}")
cari_angka = int(input("Masukkan angka yang ingin kamu cari: "))
hasil = linear_search(data, cari_angka)
if hasil != -1:
    print(f"Angka {hasil[1]} ditemukan di index ke-{hasil[0]}.")
else:
    print("Tidak ada")


def binary_search(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid, arr[mid]

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print("\n\n===== Binary Search =====")
print(f"Data:\n {merge_sort(data)}")
search_number = int(input("Masukkan angka yang ingin kamu cari: "))
result = binary_search(merge_sort(data), search_number)

if result != -1:
    print(f"Angka {result[1]} ditemukan di index ke-{result[0]}.")
else:
    print("Tidak ada")