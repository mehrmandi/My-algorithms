def palindromicStrings(n, k):
    MOD = 10**9 + 7

    res = 0
    ways = 1

    for half in range(1, (n + 1) // 2 + 1):

        if half > k:
            break

        ways = (ways * (k - half + 1)) % MOD

        # length = 2*half - 1
        if 2 * half - 1 <= n:
            res = (res + ways) % MOD

        # length = 2*half
        if 2 * half <= n:
            res = (res + ways) % MOD

    return res

n = 5
k = 8
print(palindromicStrings(n, k))
            
            
            
    
    
