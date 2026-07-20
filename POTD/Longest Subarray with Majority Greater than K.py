# def longestSubArray(arr, k):
#     n = len(arr)

#     # Step 1: Convert the array
#     transformed = [1 if num > k else -1 for num in arr]

#     # Step 2: Find the longest subarray with a positive sum
#     prefix_sum = 0
#     index_map = {0: -1}  # Store first occurrence of prefix sum
#     max_length = 0

#     for i in range(n):
#         prefix_sum += transformed[i]

#         # If prefix sum is positive, we update max_length
#         if prefix_sum > 0:
#             max_length = i + 1  # Entire array from 0 to i has a positive sum
#         print("i, prefix, index", i, prefix_sum, index_map)
#         # Store first occurrence of prefix_sum
#         if prefix_sum not in index_map:
#             index_map[prefix_sum] = i
            
#         print(index_map)

#         # If we've seen (prefix_sum - 1) before, update max_length
#         if (prefix_sum - 1) in index_map:
#             print("prefix_sum - 1********", max_length, i - index_map[prefix_sum - 1])
#             max_length = max(max_length, i - index_map[prefix_sum - 1])
            
#         print("max_length", max_length)

#     return max_length

# Using Hashing - O(n) Time and O(n) Space-------------------------
def longestSubarray(arr, k):
    n = len(arr)
    mp = {}
    ans = 0
    sum = 0

    for i in range(n):
        # Treat elements <= k as -1, > k as +1
        if arr[i] <= k:
            sum -= 1
        else:
            sum += 1

        # If sum is positive, prefix is valid
        if sum > 0:
            ans = i + 1
        else:
            # Check if prefix sum sum-1 occurred before
            if (sum - 1) in mp:
                ans = max(ans, i - mp[sum - 1])

        # Store first occurrence of this sum
        if sum not in mp:
            mp[sum] = i

    return ans


# Example Usage:
arr = [11, 60, 26, 7, 44, 30, 18, 29, 10, 72, 3, 4,
       49, 77, 23, 21, 20, 34, 20, 99, 21, 70, 9, 74, 41]
k = 35
print(longestSubArray(arr, k))  # Output: 3
    
        
    
    
    

