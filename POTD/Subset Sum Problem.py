# Given an array arr[] of non-negative integers and a value sum, the task is to check if there is a subset of the given array whose sum is equal to the given sum.


# Using Recursion – O(2 ^ n) Time and O(n) Space

# def isSumRec(arr, n, sum):
#     # Base Cases
#     if sum == 0:
#         return True
#     if n == 0:
#         return False

#     # If the last element is greater
#     # than the sum, ignore it
#     if arr[n - 1] > sum:
#         return isSubsetSumRec(arr, n - 1, sum)

#     # Check if sum can be obtained by including
#     # or excluding the last element
#     return (isSubsetSumRec(arr, n - 1, sum) or
#             isSubsetSumRec(arr, n - 1, sum - arr[n - 1]))


# def isSubsetSum(arr, sum):
#     return isSubsetSumRec(arr, len(arr), sum)


# ----------------------------------------------------
# Using Space Optimized DP – O(sum*n) Time and O(sum) Space

def isSubsetSum(arr, sum):
    n = len(arr)
    prev = [False] * (sum + 1)
    curr = [False] * (sum + 1)

    # Base case: sum 0 can always
    # be achieved
    prev[0] = True

    # Fill the dp table in a
    # bottom-up manner
    for i in range(1, n + 1):
        for j in range(sum + 1):
            if j < arr[i - 1]:
                curr[j] = prev[j]
            else:
                curr[j] = prev[j] or prev[j - arr[i - 1]]
        prev = curr.copy()

    return prev[sum]


# -----------------------------------------------------

# Using Bottom-Up DP (Tabulation) - O(sum*n) Time and O(sum*n) Space

# def isSubsetSum(arr, sum):
#     n = len(arr)
#
#     # Create a 2D list for storing
#     # results of subproblems
#     dp = [[False] * (sum + 1) for _ in range(n + 1)]
#
#     # If sum is 0, then answer is
#     # true (empty subset)
#     for i in range(n + 1):
#         dp[i][0] = True
#
#     # Fill the dp table in bottom-up manner
#     for i in range(1, n + 1):
#         for j in range(1, sum + 1):
#             if j < arr[i - 1]:
#
#                 # Exclude the current element
#                 dp[i][j] = dp[i - 1][j]
#             else:
#
#                 # Include or exclude
#                 dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
#
#     return dp[n][sum]


arr = [2, 4, 11, 10, 5]
k = 16
print(isSubsetSum(arr, k))
