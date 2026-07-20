# [Expected Approach] Greedy Stack-Based Subsequence Selection - O(n) Time and O(n) Space


def maxSubseq(s, k):
    n = len(s)
    res = ''
    del_op = k
    
    for i in range(n):
        while del_op > 0 and res and res[-1] < s[i]:
            res = res[:-1]
            del_op -= 1
            
        res += s[i]
        
    return res[:n - k]
    
        
s = "zrptllivngoi"
k = 8
print(maxSubseq(s, k))
    

        
    
    
