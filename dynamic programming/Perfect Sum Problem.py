def perfect_sum(arr, target):
    n = len(arr)
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(n + 1):
        for j in range(target + 1):

            dp[0][0] = 1

            if i == 0 and j > 0:
                dp[0][j] = 0

            elif arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]

    return dp[n][target]


arr = [35, 2, 8, 22]
k = 10

print(perfect_sum(arr, k))


    