def wordBreak(s, dictionary):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for w in dictionary:
            start = i - len(w)
            print(start, i, w)
            if start >= 0 and dp[start] and s[start:start + len(w)] == w:
                dp[i] = True
                print(dp)
                break
    return 1 if dp[n] else 0


s = "ilike"
dictionary = ["i", "like", "gfg"]
print(wordBreak(s, dictionary))