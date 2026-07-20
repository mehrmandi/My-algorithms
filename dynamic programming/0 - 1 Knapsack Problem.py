def knapSack(W, wt, val):
    n = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Driver Code
profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50

print(knapSack(W, weight, profit))


# def knapSack(W, wt, val, n):
#     # Making the dp array
#     dp = [0 for i in range(W + 1)]
#
#     # Taking first i elements
#     for i in range(1, n + 1):
#
#         # Starting from back,
#         # so that we also have data of
#         # previous computation when taking i-1 items
#         for w in range(W, 0, -1):
#             if wt[i - 1] <= w:
#                 # Finding the maximum value
#                 dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
#
#     return dp[W]
#
#
# # Driver code
# if __name__ == '__main__':
#     profit = [60, 100, 120]
#     weight = [10, 20, 30]
#     W = 50
#     n = len(profit)
#     print(knapSack(W, weight, profit, n))