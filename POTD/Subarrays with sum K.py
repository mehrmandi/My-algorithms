
def subarraySumK(arr, k):
    n = len(arr)
    res = 0
    hash = {0:1}
    prefix = 0
    
    for i in range(n):
        prefix += arr[i]
        res += hash.get(prefix - k, 0)
        hash[prefix] = hash.get(prefix, 0) + 1
        
    return res
    
    


arr = [10, 2, -2, -20, 10]
k = -10
print(subarraySumK(arr, k))
