# Given an integer array arr[] and two integers l and r, find the number of subarrays whose sum lies in the range [l, r] (inclusive). A subarray is a contiguous sequence of elements within the array.

# Using Sliding Window with Inclusion-Exclusion - O(n) Time and O(1) Space

def underSumSubarray(arr, num):
    n = len(arr)
    # Initialize variables to keep track of the count of subarrays, the current sum, and the start and end indices of the sliding window
    count = 0
    current_sum = 0
    start = 0
    end = 0
    
    # Use sliding window technique to find the count of subarrays with sum less than or equal to num
    while end < n:
        current_sum += arr[end]
        while current_sum > num and start <= end:
            current_sum -= arr[start]
            start += 1
            
        # Count the number of subarrays with sum less than or equal to num
        count += (end - start + 1)
        end += 1
        
        
    return count

def countSubarray(arr, l, r):
    # Count the number of subarrays with sum in the range [l, r] by using the helper function underSumSubarray
    # The number of subarrays with sum in the range [l, r] is equal to the number of subarrays with sum less than or equal to r minus the number of subarrays with sum less than l.
    return underSumSubarray(arr, r) - underSumSubarray(arr, l - 1)

            
 
l = 3
r = 8
arr = [1, 4, 6]
print(countSubarray(arr, l, r))

