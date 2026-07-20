def maxSum(arr):
    n = len(arr)
    dp = [0 for _ in range(n)]
    if n == 1:
        return arr[0]

    if n == 2:
        return max(arr[0], arr[1])

    dp[0], dp[1], dp[2] = arr[0], arr[1], arr[2] + arr[0]

    for i in range(3, n):
        dp[i] = max(arr[i] + dp[i - 2], arr[i] + dp[i - 3])

    return max(dp[n - 1], dp[n - 2])


arr = [3, 2, 7, 10]

print(maxSum(arr))

