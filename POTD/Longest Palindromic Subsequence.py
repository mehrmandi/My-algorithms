def lCS(S1, S2):
    m = len(S1)
    n = len(S2)

    dp = [[0] * (n + 1) for x in range(m + 1)]

    for i in range(1, m + 1):
        print("----------------------")
        print("i", i)
        for j in range(1, n + 1):
            print("j", j)
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    return dp[m][n]

def lPS(s):
    reverse = s[::-1]

    return lCS(s, reverse)



s = "bbabcbcab"
print(lPS(s))


# def longest_palindromic_subsequence(s):
#     n = len(s)
#     dp = [[0] * n for _ in range(n)]

#     for i in range(n):
#         dp[i][i] = 1  # Single character palindromes

#     for cl in range(2, n + 1):  # Length of substring
#         for i in range(n - cl + 1):
#             j = i + cl - 1
#             if s[i] == s[j]:
#                 dp[i][j] = dp[i + 1][j - 1] + 2
#             else:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

#     return dp[0][n-1]


# # Example usage:
# s = "bbabcb"
# print(longest_palindromic_subsequence(s))  # Output: 5 (e.g., "babcb")
