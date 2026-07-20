def array_search(arr, k):
    if not k in arr:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if low == high:
            return low + 1

        elif k in arr[low:mid + 1]:
            high = mid

        else:
            low = mid + 1



arr = [16, 16, 57, 16, 34, 18, 16]
k = 16
print(array_search(arr, k))