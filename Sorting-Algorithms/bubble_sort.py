def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


n = int(input("Enter the number of elements: "))
arr = [int(input("Enter element: ")) for i in range(n)]

print(f"Original array: {arr}")

bubble_sort(arr)

print(f"Sorted array: {arr}")
