def romanToDecimal(s):
    n = len(s)
    if n == 0:
        return 0
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = vals[s[n-1]]
    
    for i in range(n - 2, -1, -1):
        if vals[s[i]] >= vals[s[i + 1]]:
            res += vals[s[i]]
        else:
            res -= vals[s[i]]
    return res
        
        
s = "MCMIV"
print(romanToDecimal(s))
