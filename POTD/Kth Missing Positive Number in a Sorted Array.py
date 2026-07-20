# def kthMissing(arr, k):
#     res = 0
#     i = 1
#     max_num = max(arr)
    
#     while k > 0 and i < max_num:
#         if i not in arr:
#             res = i
#             i += 1
#             k -= 1
#         else:
#             i += 1
            
#     if k > 0:
#         res = max_num + k
        
#     return res
    
def kthMissing(arr, k):
    lo = 0
    hi = len(arr) - 1
    res = len(arr) + k

    # binary Search for index where
    # arr[i] > (i + k)
    while lo <= hi:
        mid = (lo + hi) // 2
        print(lo, hi, mid)
        if arr[mid] > mid + k:
            res = mid + k
            hi = mid - 1
        else:
            lo = mid + 1

    return res


arr = [2, 3, 4, 7, 11]
k = 5
print(kthMissing(arr, k))
    
