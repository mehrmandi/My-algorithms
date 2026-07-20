# def farMin(arr):
#     n = len(arr)
#     res = []
    
#     for i in range(n):
#         min_idx = -1
#         for j in range(i + 1, n):
#             if arr[j] < arr[i] and j > min_idx:
#                 min_idx = j
#         res.append(min_idx)
        
#     return res
                

# arr = [2, 5, 1, 3, 5]
# print(farMin(arr))

# def farMin(arr):
#     n = len(arr)
#     res = [-1 for _ in range(n)]
    
    
#     for i in range(n - 2, -1, -1):
#         if arr[i] > arr[n - 1]:
#             res[i] = n - 1
            
#         elif arr[i] <= arr[n - 1]:
#             for j in range(n - 2, i, -1):
#                 if res[j] == -1 and arr[j] < arr[i]:
#                     res[i] = j
#                     break
  
                
#     return res
                

# arr = [2, 5, 1, 3, 2]
# print(farMin(arr))
# [Expected Approach] Binary Search – O(n*log(n)) Time and O(n) Space-------------------------------
def farthest_smaller_right(arr):
    n = len(arr)
    suffix_min = [0] * n
    suffix_min[-1] = arr[-1]

    # Step 1: Build suffix minimum array
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(arr[i], suffix_min[i + 1])

    result = [-1] * n

    # Step 2: For each index, binary search for farthest j > i
    for i in range(n - 1):
        low, high = i + 1, n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if suffix_min[mid] < arr[i]:
                ans = mid
                low = mid + 1  # search farther right
            else:
                high = mid - 1
        result[i] = ans

    return result

            
arr = [2, 5, 1, 3, 2]
print(farthest_smaller_right(arr))
