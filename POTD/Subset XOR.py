def subsetXOR(n):
    all_XOR = 0
    res = [i for i in range(1, n + 1)]
    
    for i in range(1, n + 1):
        all_XOR ^= i
        
    if all_XOR == n:
        return res
    else:
        x = all_XOR ^ n
        if 1 <= x <= n:
            res.pop(x - 1)
        else:
            return [n]
        
    return res


n = 65
print(subsetXOR(n))
    