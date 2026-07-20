# from functools import lru_cache
#
#
# # @lru_cache(maxsize=1001)
# def rodCutting(price):
#     n = len(price)
#
#     dp = [price[0] * x for x in range(n + 1)]
#
#     for i in range(1, n):
#         if price[i] > dp[i + 1]:
#             for j in range(i + 1, n + 1):
#                 if j >= 3:
#                     l = j // 2
#                     for k in range(1, l + 1):
#                         dp[j] = max(dp[j], dp[k] + dp[j - k], price[j - 1])
#                 else:
#                     dp[j] = max(dp[j], price[j - 1])
#
#     return dp[n]

def cutRod(p):
    # code here

    n = len(p)

    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[j] = max(dp[j], p[i] + dp[j - i - 1])

        print(dp)

    return dp[-1]


price = [1, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(price))
