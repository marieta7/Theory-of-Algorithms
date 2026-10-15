def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


n = int(input("Enter the number of elements: "))
arr = [int(input("Enter element: ")) for i in range(n)]

print(f"Original array: {arr}")

selection_sort(arr)

print(f"Sorted array: {arr}")
