import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('vehicles.csv')

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    X = arr[left:mid + 1]
    Y = arr[mid + 1:right + 1]

    # Merge the arrays X and Y into arr
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = X[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = Y[j]
        j += 1
        k += 1


def year():
    print("test")

def price():
    print("test")
def manufacturer():
    print("test")
def condition():
    print("test")

def main():
    num_commands = int(input("Number of commands?"))
    for x in range(num_commands):
        command = input("Choose between year, price, manufacturer, and condition")
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
