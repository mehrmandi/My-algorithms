def minMaxCandy(prices, k):
    prices.sort()
    n = len(prices)
    i, j = 0, n
    max_val = 0
    min_val = 0
    
    while i < j:
        min_val += prices[i]
        j -= k
        i += 1
    
    i, j = -1, n -1
    
    while i < j:
        max_val += prices[j]
        i += k
        j -= 1
        
    return [min_val, max_val]
    
    
prices = [3, 2, 1, 4]
k = 2
print(minMaxCandy(prices, k))
