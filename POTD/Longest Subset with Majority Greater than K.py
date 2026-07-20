def longestSubGreaterK(arr, k):
    arr.sort()
    print(arr)
    n = len(arr)
    low, high = 0, n - 1
    mid = 0

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == k:
            mid = mid + 1
            break

        if arr[mid] < k:
            low = mid + 1

        elif arr[mid] > k:
            high = mid - 1
    print(mid)
    greater = n - mid
    smaller = n - greater


    if greater == 0:
        return 0

    elif smaller <= greater - 1:
        return greater + smaller

    else:
        return (2 * greater) - 1


arr = [11, 60, 26, 7, 44, 30, 18, 29, 10, 72, 3, 4, 49, 77, 23, 21, 20, 34, 20, 99, 21, 70, 9, 74, 41]
k = 35
print(longestSubGreaterK(arr, k))
