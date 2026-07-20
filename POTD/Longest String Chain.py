def longestChain(arr):
    words.sort(key=len)

    dp = {}

    res = 1

    for w in words:
        dp[w] = 1

        for i in range(len(w)):
            pred = w[:i] + w[i + 1:]
            if pred in dp:
                dp[w] = max(dp[w], dp[pred] + 1)

        res = max(res, dp[w])

    return res



words = ["ab", "cb", "abc", "adb", "abdc", "ajbdc", "adjbc"]
print(longestChain(words))