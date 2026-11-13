def partition(arr, l, r):
    pivot = arr[(l + r) // 2]
    i = l
    j = r

    while i <= j:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return j


def quick_sort(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        quick_sort(arr, l, q)
        quick_sort(arr, q + 1, r)

    return arr


n = int(input())
arr = [int(input()) for i in range(n)]

quick_sort(arr, 0, len(arr) - 1)

print(f"Sorted array: {arr}")
