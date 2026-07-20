def findRepetitiveElement(arr):
    n = len(arr)
    dp = [False for _ in range(n - 1)]

    for i in arr:
        if not dp[i - 1]:
            dp[i - 1] = True
        else:
            return i


arr = [1, 1]
print(findRepetitiveElement(arr))
