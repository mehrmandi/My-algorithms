# [Expected Approach] Space-Optimized DP - O(m*n) Time and O(m) Space-----------------


def isInterleave(s1, s2, s3):

    # If lengths don't match, return false
    if len(s1) + len(s2) != len(s3):
        return False

    n, m = len(s1), len(s2)

    # Two rows for DP
    prev = [False] * (m + 1)
    curr = [False] * (m + 1)

    # Base case
    prev[0] = True

    # Fill first row (s1 empty)
    for j in range(1, m + 1):
        prev[j] = prev[j - 1] and s2[j - 1] == s3[j - 1]

    # Fill the DP rows
    for i in range(1, n + 1):
        # first column
        curr[0] = prev[0] and s1[i - 1] == s3[i - 1]

        for j in range(1, m + 1):
            k = i + j
            curr[j] = (prev[j] and s1[i - 1] == s3[k - 1]) or \
                      (curr[j - 1] and s2[j - 1] == s3[k - 1])

        # move current row to previous
        prev = curr[:]

    return prev[m]


if __name__ == "__main__":
    s1 = "AAB"
    s2 = "AAC"
    s3 = "AAABAC"
    print("true" if isInterleave(s1, s2, s3) else "false")


# [Better Approach 2] Using Bottom-Up DP - O(m*n) Time and O(m*n) Space---------------
            
# def isInterleave(s1, s2, s3):
#     m, n = len(s1), len(s2)

#     # s3 can only be formed if total lengths match
#     if m + n != len(s3):
#         return False

#     dp = [[False] * (n + 1) for _ in range(m + 1)]
#     dp[0][0] = True

#     # Fill first row (s1 is empty)
#     for j in range(1, n + 1):
#         dp[0][j] = (s2[j - 1] == s3[j - 1]) and dp[0][j - 1]

#     # Fill first column (s2 is empty)
#     for i in range(1, m + 1):
#         dp[i][0] = (s1[i - 1] == s3[i - 1]) and dp[i - 1][0]

#     # Fill the rest of dp table
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             k = i + j - 1
#             dp[i][j] = ((s1[i - 1] == s3[k] and dp[i - 1][j]) or
#                         (s2[j - 1] == s3[k] and dp[i][j - 1]))

#     return dp[m][n]


# if __name__ == "__main__":
#     s1 = "AAB"
#     s2 = "AAC"
#     s3 = "AAAABC"
#     print("true" if isInterleave(s1, s2, s3) else "false")
