def coinChange(coins, sum):
    coins.sort()
    n = len(coins)
    dp = [0 for _ in range(sum + 1)]
    dp[0] = 1


    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]


arr = [2, 3, 8, 3, 3, 3, 2]
sum = 19

# print(check(arr, sum, 0, 4))

print(coinChange(arr, sum))
