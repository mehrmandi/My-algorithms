# Given an integer n, count the number of binary strings of length 2 * n that contain exactly n ones and n zeros such that every prefix of the string contains at least as many ones as zeros. Since the answer can be very large, return it modulo 109 + 7.

# Dynamic Programming(Catalan Numbers) - O(n ^ 2) Time and O(n) Space

def prefixStrings(n: int) -> int:
    mod = 1000000007
    if n == 0:
        return 0
    
    dp = [0 for _ in range(n + 1)]
    dp[0] = dp[1] = 1
    

    for i in range(2, n + 1):
        res = 0
        for j in range(i):
            res  = (dp[j] * dp[i - j - 1] + res) % mod
    
        dp[i] = res    
            
    return dp[n]
    


n = 4
print(prefixStrings(n))

