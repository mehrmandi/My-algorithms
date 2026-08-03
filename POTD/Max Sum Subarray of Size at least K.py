# Given an array arr[] and an integer k, find the maximum sum among all contiguous subarrays having a length greater than or equal to k

# Sliding Window with Kadane's Optimization - O(n) Time and O(1) Space

def maxSumWithK(arr: list[int], k: int) -> int:
    n = len(arr)
    if n < k:
        return False

    # Calculate the sum of the first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Initialize variables to keep track of the prefix sum and the starting index of the sliding window
    pre_sum = 0
    j = 0

    # Use sliding window technique
    for i in range(k, n):
        current_sum += arr[i]
        
        # Update the prefix sum with the element that is leaving the window
        pre_sum += arr[j]
        j += 1
        
        max_sum = max(max_sum, current_sum)
        
        # If the prefix sum is negative, we can discard it to potentially increase the maximum sum of the subarray
        if pre_sum < 0:
            current_sum -= pre_sum
            max_sum = max(max_sum, current_sum)
            # Reset the prefix sum
            pre_sum = 0

    return max_sum


arr = [-2, -5, 1, 2, 3, 5, 8, 4, 1, 0, -2, -5, 32, -5, -2]
k = 3
print(maxSumWithK(arr, k))
