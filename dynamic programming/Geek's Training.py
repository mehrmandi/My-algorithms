def maximumPoints(mat):
    # Code here
    n = len(mat)

    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(3):

            for k in range(3):
                if k == j:
                    continue

                dp[i][j] = max(dp[i][j], dp[i + 1][k])

            dp[i][j] += mat[i][j]
            

    return max(dp[0][0], dp[0][1], dp[0][2])


arr = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]

print(maximumPoints(arr))