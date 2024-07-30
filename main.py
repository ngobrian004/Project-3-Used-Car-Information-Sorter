import pandas as pd
import time

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('vehicles.csv')

price = df["price"].to_numpy()
year = df["year"].to_numpy()
manufacturer = df["manufacturer"].to_numpy()
condition = df["condition"].to_numpy()

data = [price, year, manufacturer, condition]


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    x = arr[left:mid + 1]
    y = arr[mid + 1:right + 1]

    # Merge the arrays X and Y into arr
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if x[i] <= y[j]:
            arr[k] = x[i]
            i += 1
        else:
            arr[k] = y[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = x[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = y[j]
        j += 1
        k += 1


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
    if right < n & arr[left] < arr[larger]:
        larger = right

    if larger != i:
        temp = arr[larger]
        arr[larger] = arr[i]
        arr[i] = temp
        i = larger
        heapify(arr, n, i)


def year():
    start = time.time()
    print("test")
    end = time.time()
    length = end - start
    print("Heap sort:", length, "seconds")
    start = time.time()

    end = time.time()
    length = end - start
    print("Merge sort:", length, "seconds")


def price():
    print("test")


def manufacturer():
    print("test")


def condition():
    print("test")


def main():
    num_commands = int(input("Number of commands? "))
    for x in range(num_commands):
        command = input("Choose between year, price, manufacturer, and condition: ")
        if command == "year":
            year()
        elif command == "price":
            price()
        elif command == "manufacturer":
            manufacturer()
        elif command == "condition":
            condition()
        else:
            print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
