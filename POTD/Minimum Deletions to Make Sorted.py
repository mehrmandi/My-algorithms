# Using LIS Tabulation – O(n ^ 2) Time and O(n) Space-----------------------------------

# def minDeletions(arr):
#     n = len(arr)
    
#     # array to store the length of the longest increasing subsequence ending at each index
#     counter = [1 for _ in range(n)]
    
#     # iterate through the array to find the length of the longest increasing subsequence
#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 # update the counter for the current index based on the previous indices
#                 counter[i] = max(counter[i], counter[j] + 1)
#     # find the minimum number of deletions required to make the array sorted by subtracting the length of the longest increasing subsequence from the total length of the array            
#     res = n - max(counter)
    
#     # return the result           
#     return res


# Patience Sorting(LIS with Binary Search) - O(n log n) Time and O(n) Space-----------------------

from bisect import bisect_left

def minDeletions(arr):
    n = len(arr)
    
    # array to store sorted elements
    ordered_arr = []
    
    # traverse array to find increasing elements
    for i in range(n):
        # find the position of the current element in the ordered array using binary search
        position = bisect_left(ordered_arr, arr[i])
        
        # if the position is equal to the length of the ordered array, it means the current element is greater than all elements in the ordered array, so we append it to the end of the ordered array
        if position == len(ordered_arr):
            ordered_arr.append(arr[i])
        
        # otherwise, we replace the element at the found position with the current element to maintain the order of the ordered array    
        else:
            ordered_arr[position] = arr[i]
 
    # return minimum deletions
    return n - len(ordered_arr)


arr = [5, 6, 1, 7, 4]
print(minDeletions(arr))
