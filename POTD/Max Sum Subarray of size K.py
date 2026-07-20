# def maxSubarraySum(arr, k):
#     n = len(arr)
#     low = 0
#     res = 0
    
#     while low + k <= n:
#         res = max(res, sum(arr[low:low + k]))
#         low += 1
        
#     return res

# [Expected Approach] Optimized Sliding Window - O(n) Time and O(1) Space------------
def maxSubarraySum(arr, k):
    n = len(arr)
    res = sum(arr[:k])
    prev = res
    
    for i in range(k, n):
        prev = prev + arr[i] - arr[i - k]
        res = max(res, prev)
        
    return res
        

arr = [100, 200, 300, 400]
k = 2
print(maxSubarraySum(arr, k))
