def noOfWays(self, m, n, x):
    # code here
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, x + 1):
            # Ensure k does not exceed face value
            for k in range(1, min(m + 1, j + 1)):
                dp[i][j] += dp[i-1][j-k]

    return dp[n][x]
