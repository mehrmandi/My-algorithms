def maximum_bitonic(arr):
    low, high = 0, len(arr) - 1

    if arr[high] > arr[high - 1]:
        return arr[high]

    if arr[0] > arr[1]:
        return arr[0]

    while True:
        mid = low + (high - low) // 2

        if arr[mid - 1] < arr[mid] < arr[mid + 1]:
            low = mid + 1

        elif arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]

        else:
            high = mid - 1



arr = [120, 100, 80, 20, 0]

print(maximum_bitonic(arr))


