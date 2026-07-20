def is_valid(arr, k, max_sum):
    count = 1
    curr_sum = 0
    
    for num in arr:
        if curr_sum + num > max_sum:
            count += 1
            curr_sum = num
        else:
            curr_sum += num
            
    return count <= k

def minMaxSubarray(arr, k):
    low = max(arr)
    high = sum(arr)
    res = high
    
    while low <= high:
        mid = (low + high) // 2
        if is_valid(arr, k, mid):
            result = mid
            high = mid - 1     
        else:
            low = mid + 1
            
    return result
            
    

# Example
arr = [1, 2, 3, 4]
k = 3
print(minimize_max_subarray_sum(arr, k))  # Output: 4

