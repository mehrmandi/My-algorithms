def maxGold(mat):
    n = len(mat)
    m = len(mat[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        dp[0][i] = mat[i][0]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = mat[j][i] + max(dp[i - 1][j], dp[i - 1][j + 1])

            elif j == n - 1:
                dp[i][j] = mat[j][i] + max(dp[i - 1][j], dp[i - 1][j - 1])

            else:
                dp[i][j] = mat[j][i] + max(dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1])
        print(dp)

    return max(dp[m - 1])


mat = [[1, 3, 3], [2, 1, 4],[0, 7, 5]]
print(maxGold(mat))





