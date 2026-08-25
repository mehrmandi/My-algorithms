# Given two arrays, a[] and b[], find the length of the longest common increasing subsequence(LCIS).
# A subsequence is a sequence that appears in the same relative order in both arrays, but not necessarily consecutively.

# The Longest Common Increasing Subsequence(LCIS) is defined as the longest sequence that appears in both arrays and whose elements are in strictly increasing order.

# [Expected Approach] Using 1D Dp - O(m*n) Time and O(n) Space--------------

def lCIS(a, b):
    m = len(a)
    n = len(b)

    # dp[j] stores the length of LCIS ending at b[j]
    dp = [0] * n

    # Traverse each element of array a
    for i in range(m):
        currentLength = 0

        # Compare current element of a with all elements of b
        for j in range(n):

            # When elements match, extend the LCIS
            if a[i] == b[j]:
                dp[j] = max(dp[j], currentLength + 1)

            # If a[i] is greater, update best LCIS so far
            elif a[i] > b[j]:
                currentLength = max(currentLength, dp[j])

    # The maximum value in dp gives final LCIS length
    return max(dp)


a = [3, 4, 9, 1]
b = [5, 3, 8, 9, 10, 2, 1]
print(lCIS(a, b))
