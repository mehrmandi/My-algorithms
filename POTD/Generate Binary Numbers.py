def generateBinary(n):
    res = []
    
    for i in range(1, n + 1):
        bin_str = ""
        val = i
        while val // 2 > 0:
            new_val = val // 2
            remain = str(val % 2)
            bin_str = remain + bin_str
            val = new_val
        remain = str(val % 2)
        bin_str = remain + bin_str
        res.append(bin_str)
        
    return res

n = 4
print(generateBinary(n))
            
            
