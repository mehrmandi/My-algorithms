def countDistinct(arr, k):
    hash = {}
    res = []
    n = len(arr)
    
    for i in range(k):
        hash[arr[i]] = hash.get(arr[i], 0) + 1
    
    res.append(len(hash))
    
    for i in range(k, n):
        hash[arr[i]] = hash.get(arr[i], 0) + 1
        hash[arr[i - k]] = hash.get(arr[i - k], 0) - 1
        
        if hash[arr[i - k]] == 0:
            hash.pop(arr[i - k])
        
        res.append(len(hash))
            
    
    return res


arr = [1, 1, 1, 1, 1]
k = 3
print(countDistinct(arr, k))
