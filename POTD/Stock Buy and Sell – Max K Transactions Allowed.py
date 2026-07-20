# def maxProfit(arr, k):
#     n = len(arr)
#     dp = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
#
#
#     for i in range(n -1):
#         for j in range(n - 1):
#             for


def maximumProfit(prices):
    res = 0

    # Keep on adding the difference between
    # adjacent when the prices a
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            res += prices[i] - prices[i - 1]

    return res













arr = [4, 70, 3, 45, 55, 35, 90]
k = 3
print(maxProfit(arr, k))
# [0 , 0],  [1, 1 ], [2 , 2] , [3 , 3], [4, 4], [5, 5], [0, 2], [1, 3], [2, 4], [3, 5]j
