
def maxSubarrayXOR(arr, k):
    n = len(arr)
    prev = arr[0]
    
    for i in range(1, k):
        prev ^= arr[i]
        
    res = prev
        
    for i in range(k, n):
        prev = (prev ^ arr[i]) ^ arr[i - k]
        res = max(prev, res)
        
    return res
        

arr = [1, 2, 4, 5, 6]
k = 2
print(maxSubarrayXOR(arr, k))
