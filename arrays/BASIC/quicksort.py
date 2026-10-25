def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]          # Choose last element as pivot
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)


arr = list(map(int, input().split()))
print(quicksort(arr))

#if not asked in place


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


arr = list(map(int, input().split()))
quicksort(arr, 0, len(arr) - 1)
print(arr)