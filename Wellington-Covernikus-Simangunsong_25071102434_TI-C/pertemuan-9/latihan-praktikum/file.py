"""Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan, yaitu Insertion Sort , Quick Sort dan Counting Sort secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
Implementasikan fungsi terpisah untuk 

Insertion Sort , Quick Sort dan Counting Sort.
Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma."""


jumlah = int(input("Masukkan jumlah bilangan bulat: "))
array = []
while len(array) < jumlah:
    input_bilangan = int(input("Masukkan bilangan (non-negatif): "))
    if input_bilangan < 0:
        print("Bilangan tidak boleh negatif!")
    else:
        array.append(input_bilangan)

print(f"Daftar bilangan: {array}")

def insertion_sort(arr):
    insertion_arr = arr.copy()
    n = len(insertion_arr)
    for i in range(1,n):
        insert_index = i
        current_value = insertion_arr[i]
        for j in range(i-1, -1, -1):
            if insertion_arr[j] > current_value:
                insertion_arr[j+1] = insertion_arr[j]
                insert_index = j
            else:
                break
        insertion_arr[insert_index] = current_value
    return insertion_arr

print(f"\nBilangan sebelum diurutkan: {array}")
print(f"Bilangan setelah diurutkan (insertion sort): {insertion_sort(array)}")


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(quick_sort_arr, low=0, high=None):
    if high is None:
        high = len(quick_sort_arr) - 1

    if low < high:
        pivot_index = partition(quick_sort_arr, low, high)
        quick_sort(quick_sort_arr, low, pivot_index-1)
        quick_sort(quick_sort_arr, pivot_index+1, high)
    return quick_sort_arr

print(f"\nBilangan sebelum diurutkan: {array}")
print(f"Bilangan setelah diurutkan (quick sort): {quick_sort(array)}")


def counting_sort(arr):
    quick_sort_arr = arr.copy()
    max_val = max(quick_sort_arr)
    count = [0] * (max_val + 1)

    while len(quick_sort_arr) > 0:
        num = quick_sort_arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            quick_sort_arr.append(i)
            count[i] -= 1
    return quick_sort_arr

print(f"\nBilangan sebelum diurutkan: {array}")
print(f"Bilangan setelah diurutkan (counting sort): {counting_sort(array)}")