import pandas as pd
import time


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('vehicles.csv')

price_arr = df["price"].to_numpy()
year_arr = df["year"].to_numpy()
manufacturer_arr = df["manufacturer"].to_numpy()
condition_arr = df["condition"].to_numpy()

data = [price_arr, year_arr, manufacturer_arr, condition_arr]

def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)

def partition(array, low, high):
    pivot = array[low]
    up = low
    down = high

    while up < down:
        for j in range(up, high):
            if array[up] > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if array[down] < pivot:
                break
            down -= 1
        if up < down:
            array[up], array[down] = array[down], array[up]

        array[low], array[down] = array[down], array[low]
        return down

def merge(arr, left, mid, right):
    # Create X ← arr[left..mid] & Y ← arr[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid

    x = [0] * n1
    y = [0] * n2

    for i in range(n1):
        x[i] = arr[left + i]
    for j in range(n2):
        y[j] = arr[mid + 1 + j]

    # Merge the arrays X and Y into arr
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if x[i] <= y[j]:
            arr[k] = x[i]
            i += 1
        else:
            arr[k] = y[j]
            j += 1
        k += 1

    # When we run out of elements in either X or Y append the remaining elements
    while i < n1:
        arr[k] = x[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = y[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        # mid is the point where the array is divided into two sub-arrays
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted sub-arrays
        merge(arr, left, mid, right)


def heap_sort(arr, n):
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapify(arr, i, 0)


def heapify(arr, n, i):
    larger = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    if left < n and arr[left] > arr[larger]:
        larger = left
    if right < n and arr[right] > arr[larger]:
        larger = right

    if larger != i:
        temp = arr[larger]
        arr[larger] = arr[i]
        arr[i] = temp
        i = larger
        heapify(arr, n, i)


def year(arr):
    heap_copy = arr.copy()
    merge_copy = arr.copy()
    quick_copy = arr.copy()
    start = time.time()
    heap_sort(heap_copy, len(heap_copy))
    end = time.time()
    length = end - start
    print("\nHeap sort:", length, "seconds")

    print("Number of cars for each year (Heap Sort):")
    year_count_heap = {}
    for x in heap_copy:
        if x in year_count_heap:
            year_count_heap[x] += 1
        else:
            year_count_heap[x] = 1
    for year in year_count_heap.keys():
        print(f"{year}: {year_count_heap[year]} cars")

    start = time.time()
    merge_sort(merge_copy, 0, len(merge_copy) - 1)
    end = time.time()
    length = end - start
    print("\nMerge sort:", length, "seconds")

    print("Number of cars for each year (Merge Sort):")
    year_count_merge = {}
    for x in merge_copy:
        if x in year_count_merge:
            year_count_merge[x] += 1
        else:
            year_count_merge[x] = 1
    for year in year_count_merge.keys():
        print(f"{year}: {year_count_merge[year]} cars")

    start = time.time()
    n = len(quick_copy)
    quick_sort(quick_copy, 0, n-1)
    end = time.time()
    length = end - start
    print("\nQuick sort:", length, "seconds")

    print("Number of cars for each year (Quick Sort):")
    year_count_quick = {}
    for x in quick_copy:
        if x in year_count_quick:
            year_count_quick[x] += 1
        else:
            year_count_quick[x] = 1
    for year in year_count_quick.keys():
        print(f"{year}: {year_count_quick[year]} cars")

    if (merge_copy == quick_copy).all():
        print("\nSuccess\n")
    else:
        print("\nFailed\n")


def price(arr):
    heap_copy = arr.copy()
    merge_copy = arr.copy()

    start = time.time()
    heap_sort(heap_copy, len(heap_copy))
    end = time.time()
    length = end - start
    print("\nHeap sort:", length, "seconds")

    print("\nNumber of cars for each price category (Heap Sort):")
    price_count_heap = {}
    for x in heap_copy:
        category = (x // 10000) * 10000
        if category in price_count_heap:
            price_count_heap[category] += 1
        else:
            price_count_heap[category] = 1
    for category in price_count_heap.keys():
        print(f"${category} - ${category + 9999}: {price_count_heap[category]} cars")



    start = time.time()
    merge_sort(merge_copy, 0, len(merge_copy) - 1)
    end = time.time()
    length = end - start
    print("\nMerge sort:", length, "seconds")

    print("\nNumber of cars for each price category (Merge Sort):")
    price_count_merge = {}
    for x in merge_copy:
        category = (x // 10000) * 10000
        if category in price_count_merge:
            price_count_merge[category] += 1
        else:
            price_count_merge[category] = 1
    for category in price_count_merge.keys():
        print(f"${category} - ${category + 9999}: {price_count_merge[category]} cars")

    if (merge_copy == heap_copy).all():
        print("\nSuccess\n")
    else:
        print("\nFailed\n")


def manufacturer(arr):
    heap_copy = arr.copy()
    merge_copy = arr.copy()

    start = time.time()
    heap_sort(heap_copy, len(heap_copy))
    end = time.time()
    length = end - start
    print("\nHeap sort:", length, "seconds")

    print("\nNumber of cars for each manufacturer (Heap Sort):")
    manufacturer_count_heap = {}
    for x in heap_copy:
        if x in manufacturer_count_heap:
            manufacturer_count_heap[x] += 1
        else:
            manufacturer_count_heap[x] = 1
    for category in manufacturer_count_heap.keys():
        print(f"{category.title()}: {manufacturer_count_heap[category]} cars")

    start = time.time()
    merge_sort(merge_copy, 0, len(merge_copy) - 1)
    end = time.time()
    length = end - start
    print("\nMerge sort:", length, "seconds")

    print("\nNumber of cars for each manufacturer  (Merge Sort):")
    manufacturer_count_merge = {}
    for x in merge_copy:
        if x in manufacturer_count_merge:
            manufacturer_count_merge[x] += 1
        else:
            manufacturer_count_merge[x] = 1
    for category in manufacturer_count_merge.keys():
        print(f"{category.title()}: {manufacturer_count_merge[category]} cars")

    if (merge_copy == heap_copy).all():
        print("\nSuccess\n")
    else:
        print("\nFailed\n")


def condition(arr):
    heap_copy = arr.copy()
    merge_copy = arr.copy()
    dict_order = ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']

    start = time.time()
    heap_sort(heap_copy, len(heap_copy))
    end = time.time()
    length = end - start
    print("\nHeap sort:", length, "seconds")

    print("\nNumber of cars in each condition (Heap Sort):")
    condition_count_heap = {}
    for x in heap_copy:
        if x in condition_count_heap:
            condition_count_heap[x] += 1
        else:
            condition_count_heap[x] = 1
    res = {key: condition_count_heap[key] for key in dict_order}
    for category in res.keys():
        print(f"{category.title()}: {condition_count_heap[category]} cars")

    start = time.time()
    merge_sort(merge_copy, 0, len(merge_copy) - 1)
    end = time.time()
    length = end - start
    print("\nMerge sort:", length, "seconds")

    print("\nNumber of cars in each condition (Merge Sort):")
    condition_count_merge = {}
    for x in merge_copy:
        if x in condition_count_merge:
            condition_count_merge[x] += 1
        else:
            condition_count_merge[x] = 1
    res = {key: condition_count_heap[key] for key in dict_order}
    for category in res.keys():
        print(f"{category.title()}: {condition_count_merge[category]} cars")

    if (merge_copy == heap_copy).all():
        print("\nSuccess\n")
    else:
        print("\nFailed\n")


def main():
    while True:
        num_commands = input("Number of commands? ")
        if num_commands.isnumeric():
            num_commands = int(num_commands)
            break
        else:
            print("That is not a valid input.")
            continue

    for x in range(num_commands):
        command = input("Choose between year, price, manufacturer, and condition: ").lower()
        if command == "year":
            year(year_arr)
        elif command == "price":
            price(price_arr)
        elif command == "manufacturer":
            manufacturer(manufacturer_arr)
        elif command == "condition":
            condition(condition_arr)
        else:
            print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
