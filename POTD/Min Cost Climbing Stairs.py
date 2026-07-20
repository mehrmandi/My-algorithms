def minCost(arr):
    n = len(arr)
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = arr[0], arr[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + arr[i]

    return min(dp[n - 1], dp[n - 2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCost(cost))



