def findMinDiff(arr, M):
    n = len(arr)
    arr.sort()
    if M > n:
        return 0
    
    res = float('inf')
    
    for i in range(n - M + 1):
        res = min(res, arr[i + M - 1] - arr[i])
        
    return res


arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(findMinDiff(arr, m))
