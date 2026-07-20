def lCS(S1, S2):
    m = len(S1)
    n = len(S2)

    # Initializing a matrix of size (m+1)*(n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Building dp[m+1][n+1] in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    return dp[m][n]


def minSuperSeq(s1, s2):
    n = len(s1)
    m = len(s2)
    
    return n + m - lCS(s1, s2)


s1 = "geek"
s2 = "ek"

print(minSuperSeq(s1, s2))
