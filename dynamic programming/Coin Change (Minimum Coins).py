def coinChange(coins, sum):
    coins.sort()
    while coins[0] == 0:
        coins.pop(0)

    print(coins)

    n = len(coins)
    dp = [0 for _ in range(sum + 1)]
    if sum == 0:
        return 0

    for i in range(n):
        for j in range(coins[i], sum + 1):
            if i == 0:
                if j % coins[i] == 0:
                    dp[j] = j // coins[i]
            else:
                new_value = 0
                if dp[j - coins[i]] or not j % coins[i]:
                    new_value = 1 + dp[j - coins[i]]
                    if dp[j]:
                        dp[j] = min(dp[j], new_value)
                    else:
                        dp[j] = new_value

    if not dp[sum]:
        return -1
    else:
        return dp[sum]


coins = [638, 414, 105, 0, 0, 325, 315, 209, 24, 68, 409, 611]
sum = 845
print(coinChange(coins, sum))

#638 414 105 0 325 315 209 24 68 409 611
#
# 845