def min_item(arr):
    low, high = 0, len(arr) - 1

    if arr[low] < arr[high]:
        return arr[0]

    while low < high:
        mid = low + (high - low) // 2

        if arr[high] > arr[mid]:
            high = mid

        else:
            low = mid + 1

    return arr[low]


arr = [95, 96]

print(min_item(arr))
