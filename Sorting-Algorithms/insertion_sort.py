def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


n = int(input("Enter the number of elements: "))

arr = [int(input(f"Enter element: ")) for i in range(n)]

print(f"Original array: {arr}")

insertion_sort(arr)

print(f"Sorted array: {arr}")
