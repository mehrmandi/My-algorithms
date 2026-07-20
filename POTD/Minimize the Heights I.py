def getMinDiff(arr, k):
    arr.sort()
    n = len(arr)
    res = arr[n - 1] - arr[0]

    for i in range(1, n):
        min_val = min(arr[0] + k, arr[i] - k)
        max_val = max(arr[n - 1] - k, arr[i - 1] + k)
        res = min(res, max_val - min_val)

    return res


k = 2
arr = [1, 5, 8, 10]
print(getMinDiff(arr, k))
