
def missingRange(arr, low, high):
    s = set(arr)
    res = []
    for i in range(low, high + 1):
        if i not in s:
            res.append(i)
        
    return res
            
        
    


arr = [10, 2, 7, 1, 2, 6, 6, 4, 1]
low = 5
high = 7
print(missingRange(arr, low, high))
