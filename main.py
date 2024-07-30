import pandas as pd
import time

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('vehicles.csv')

price_arr = df["price"].to_numpy()
year_arr = df["year"].to_numpy()
manufacturer_arr = df["manufacturer"].to_numpy()
condition_arr = df["condition"].to_numpy()

data = [price_arr, year_arr, manufacturer_arr, condition_arr]


def merge(arr, left, mid, right):
    # Create X ← arr[left..mid] & Y ← arr[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid

    X = [0] * n1
    Y = [0] * n2

    for i in range(n1):
        X[i] = arr[left + i]
    for j in range(n2):
        Y[j] = arr[mid + 1 + j]

    # Merge the arrays X and Y into arr
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
        k += 1

    # When we run out of elements in either X or Y append the remaining elements
    while i < n1:
        arr[k] = X[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = Y[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        # mid is the point where the array is divided into two subarrays
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted subarrays
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

    if left < n & arr[left] < arr[larger]:
        larger = left
    if right < n & arr[right] < arr[larger]:
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
    start = time.time()
    heap_sort(heap_copy, len(heap_copy))
    end = time.time()
    length = end - start
    print("\nHeap sort:", length, "seconds")

    print("Number of cars for each year (Heap Sort):")
    year_count_heap = {}
    for y in heap_copy:
        if y in year_count_heap:
            year_count_heap[y] += 1
        else:
            year_count_heap[y] = 1
    for year in sorted(year_count_heap.keys()):
        print(f"{year}: {year_count_heap[year]} cars")



    start = time.time()
    merge_sort(merge_copy, 0, len(merge_copy) - 1)
    end = time.time()
    length = end - start
    print("\nMerge sort:", length, "seconds")

    print("Number of cars for each year (Merge Sort):")
    year_count_merge = {}
    for y in merge_copy:
        if y in year_count_merge:
            year_count_merge[y] += 1
        else:
            year_count_merge[y] = 1
    for year in sorted(year_count_merge.keys()):
        print(f"{year}: {year_count_merge[year]} cars")
    # prints out every year for merge copy (used for testing)
    print("\nPrices after Merge Sort:")
    for year in merge_copy:
        print(year)


    if (merge_copy == heap_copy).all():
        print("\nSuccess")
    else:
        print("\nFailed")


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
    for y in heap_copy:
        category = (y // 10000) * 10000
        if category in price_count_heap:
            price_count_heap[category] += 1
        else:
            price_count_heap[category] = 1
    for category in sorted(price_count_heap.keys()):
        print(f"${category} - ${category + 9999}: {price_count_heap[category]} cars")

    #prints out every price for heap copy (used for testing)
    #print("\nPrices after Heap Sort:")
    #for prices in heap_copy:
        #print(prices)

    start = time.time()
    merge_sort(merge_copy, 0, len(merge_copy) - 1)
    end = time.time()
    length = end - start
    print("\nMerge sort:", length, "seconds")

    print("\nNumber of cars for each price category (Merge Sort):")
    price_count_merge = {}
    for y in merge_copy:
        category = (y // 10000) * 10000
        if category in price_count_merge:
            price_count_merge[category] += 1
        else:
            price_count_merge[category] = 1
    for category in sorted(price_count_merge.keys()):
        print(f"${category} - ${category + 9999}: {price_count_merge[category]} cars")

    if (merge_copy == heap_copy).all():
        print("\nSuccess")
    else:
        print("\nFailed")


def manufacturer():
    print("test")


def condition():
    print("test")


def main():
    num_commands = int(input("Number of commands? "))
    for x in range(num_commands):
        command = input("Choose between year, price, manufacturer, and condition: ")
        if command == "year":
            year(year_arr)
        elif command == "price":
            price(price_arr)
        elif command == "manufacturer":
            manufacturer()
        elif command == "condition":
            condition()
        else:
            print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
