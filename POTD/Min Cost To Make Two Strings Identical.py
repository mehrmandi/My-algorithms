# Given two strings s1 and s2, and two integers costS1 and costS2, where costS1 is the cost of deleting one character from s1 and costS2 is the cost of deleting one character from s2, find the minimum cost required to make the two strings identical.

# You can delete any number of characters from either string, but the order of the remaining characters must be preserved.


# Using Space Optimized Dynamic Programming - O(n * m) Time and O(nm) Space


def lCS(S1, S2):
    m = len(S1)
    n = len(S2)

    dp = [[0] * (n + 1) for x in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    return dp[m][n]


def findMinCost(s1: str, s2: str, costS1: int, costS2: int) -> int:
    lCS_char = lCS(s1, s2)
    s1_del_char = len(s1) - lCS_char
    s2_del_char = len(s2) - lCS_char
    
    min_cost = s1_del_char * costS1 + s2_del_char * costS2
    
    return min_cost


s1 = "ef"
s2 = "gh"
costS1 = 10
costS2 = 20

print(findMinCost(s1, s2, costS1, costS2))

