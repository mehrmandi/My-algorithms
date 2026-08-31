
def minCost(n: int, i: int, d: int, c: int) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[1] = i
    
    
    for j in range(2, n + 1):
        new_add = dp[j - 1] + i
        
        minus_extra = 0 if j % 2 == 0 else 1

        new_minus = dp[j // 2 + minus_extra] + c + minus_extra * d
        
        dp[j] = min(new_add, new_minus)
            
    return dp[n]


n = 9
i = 10
d = 1
c = 1

print(minCost(n, i, d, c))
