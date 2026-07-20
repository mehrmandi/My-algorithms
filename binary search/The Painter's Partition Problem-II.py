def check(arr, k, timeLimit):
    cnt = 1
    timeSum = 0
    for time in arr:
        if timeSum + time > timeLimit:
            cnt += 1
            timeSum = time
        else:
            timeSum += time

    return cnt <= k

def min_time(arr, k):
    low = max(arr)
    high = sum(arr)
    res = -1

    if k > len(arr):
        return low

    if k == 1:
        return high


    while low <= high:
        mid = low + (high - low) // 2

        if check(arr, k, mid):
            res = mid
            high = mid - 1

        else:
            low = mid + 1

    return res


arr = [100, 200, 300, 400]
k = 1
print(min_time(arr, k))


