def search_sorted_rotated(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == k:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= k < arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if arr[mid] < k <= arr[high]:

                low = mid + 1

            else:
                high = mid - 1

    return -1


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
k = 3

print(search_sorted_rotated(arr, k))
