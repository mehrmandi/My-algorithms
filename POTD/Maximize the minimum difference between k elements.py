def is_possible(arr, k, mid):
    count = 1
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - last >= mid:
            count += 1
            last = arr[i]
        if count == k:
            return True
    return False



def max_min_diff(arr, k):
    arr.sort()
    low, high = 0, arr[-1] - arr[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        if is_possible(arr, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result
            

arr = [1, 2, 3, 10, 12, 45]
k = 5
print(max_min_diff(arr, k))


