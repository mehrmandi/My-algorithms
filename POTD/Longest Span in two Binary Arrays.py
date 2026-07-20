def longestSpan(a1, a2):
    n = len(a1)
    dp = [a1[i] - a2[i] for i in range(n)]
    max_len = 0
    hash_map = {0: -1}
    prefix_sum = 0
    
    for i in range(n):
        prefix_sum += dp[i]
        
        if prefix_sum in hash_map:
            max_len = max(max_len, i - hash_map[prefix_sum])
        
        else:
            hash_map[prefix_sum] = i
            
    return max_len
    
             


a1 = [0, 1, 1, 0, 0, 0]
a2 = [1, 0, 1, 1, 1, 1]
print(longestSpan(a1, a2))
