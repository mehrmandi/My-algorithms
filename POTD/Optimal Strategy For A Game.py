# [Expected Approach 2] Using Bottom-Up DP(Tabulation) – O(n*n) Time and O(n*n) Space--------------------------


# def maximumAmount(arr):
#     n = len(arr)
#     dp = [[0] * n for _ in range(n)]

#     # Fill table using above
#     # recursive formula.
#     for gap in range(n):
#         print("gap", gap)
#         for i in range(n - gap):
#             j = i + gap
#             print("i", i, j)
#             print(dp)

#             x = dp[i + 2][j] if (i + 2) <= j else 0
#             y = dp[i + 1][j - 1] if (i + 1) <= (j - 1) else 0
#             z = dp[i][j - 2] if i <= (j - 2) else 0
#             print("x, y, z", x, y, z)

#             dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
#             print(dp)

#     return dp[0][n - 1]

# arr = [8, 15, 3, 7]
# print(maximumAmount(arr))

# [Space Optimised] O(n ^ 2) Time and O(n) Space------------------

def maximumAmount(arr):

    n = len(arr)
    sum_val = 0
    dp = [0] * n

    for i in range(n - 1, -1, -1):

        # Calculating the sum of all the elements
        sum_val += arr[i]

        for j in range(i, n):
            if i == j:

                # If there is only one element
                dp[j] = arr[j]
            else:
                # Calculating the dp states using the relation
                dp[j] = max(arr[i] - dp[j], arr[j] - dp[j - 1])

    # Return the final result
    return (sum_val + dp[n - 1]) // 2


if __name__ == "__main__":
    arr = [5, 3, 7, 10]
    print(maximumAmount(arr))
