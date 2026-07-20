def lCSThree(s1, s2, s3):
    m = len(s1)
    n = len(s2)
    o = len(s3)

    # Initializing a matrix of size (m+1)*(n+1)
    dp = [[0] * (o + 1) for _ in range(n + 1)]

    # Building dp[m+1][n+1] in bottom-up fashion
    for i in range(1, m + 1):
        sub_dp = [[0] * (o + 1) for _ in range(n + 1)]
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    sub_dp[j][k] = dp[j - 1][k - 1] + 1
                else:
                    sub_dp[j][k] = max(dp[j][k], sub_dp[j - 1][k], sub_dp[j][k - 1])
        dp = sub_dp

    return dp[n][o]


s1 = "abcd1e2"
s2 = "bc12ea"
s3 = "bd1ea"
print(lCSThree(s1, s2, s3))

    
    
