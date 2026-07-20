
def findMaxSum(arr):
    n = len(arr)

    if n == 1:
        return arr[-1]

    if n == 2:
        return max(arr[0], arr[1])

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

    return dp[-1]


arr = [4, 4, 4, 4]

print(findMaxSum(arr))

