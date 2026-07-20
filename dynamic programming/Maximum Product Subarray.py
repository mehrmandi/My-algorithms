# def max_product(arr):
#     n = len(arr)
#     max_val = -float('inf')
#
#     dp = [[0 for j in range(n - i)] for i in range(n)]
#
#     for i in range(n):
#         dp[i][0] = arr[i]
#         for j in range(1, n - i):
#             dp[i][j] = dp[i][j - 1] * arr[j + i]
#
#         max_val = max(max_val, max(dp[i]))
#
#     return max_val

# def max_product(arr):
#     n = len(arr)
#     dp = [0 for _ in range(n)]
#     max_value = max(float("-inf"), arr[0])
#
#     for i in range(n):
#         dp[0] = arr[i]
#         for j in range(1, n - i):
#             dp[j] = dp[j - 1] * arr[j + i]
#             max_value = max(max_value, dp[j])
#
#     return max_value

def max_product(arr):

    n = len(arr)
    currMax = arr[0]

    currMin = arr[0]

    maxProd = arr[0]

    for i in range(1, n):
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)

        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)

        currMax = temp

        maxProd = max(maxProd, currMax)

    return maxProd






arr = [-2, 6, -3, -10, 0, 2]
print(max_product(arr))