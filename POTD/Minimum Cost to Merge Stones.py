def mergeStones(stones, k):
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]

    # dp[i][j] = min cost to merge i..j into x piles (only track for active x)
    INF = float('inf')
    dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i][1] = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            for m in range(2, k + 1):
                for t in range(i, j, k - 1):
                    dp[i][j][m] = min(dp[i][j][m],
                                      dp[i][t][1] + dp[t + 1][j][m - 1])

            if dp[i][j][k] < INF:
                dp[i][j][1] = dp[i][j][k] + (prefix[j + 1] - prefix[i])

    return dp[0][n - 1][1]

    
   
stones = [4, 5, 8, 7, 3, 9, 1, 5, 7]
k = 3
# 24
print(mergeStones(stones, k))
