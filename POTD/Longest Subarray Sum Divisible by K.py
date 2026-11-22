# Given an arr[] of integers and a positive integer k, find the longest subarray's length with the sum of the elements divisible by k.

# Prefix Sum modulo k - O(n) Time and O(min(n, k)) Space

def longestSubarrayDivK(arr, k):
    n = len(arr)
    ans = 0
    prefix = {}
    sum = 0

    for i in range(n):
        # prefix sum mod k
        sum = (sum + arr[i]) % k
        
        # If sum == 0, then update result with the
        # length of subarray arr[0...i]
        if sum == 0:
            ans = i + 1
        
        # Update max length for repeating sum
        elif sum in prefix:
            ans = max(ans, i - prefix[sum])
            
        # Store the first occurrence of sum
        else:
            prefix[sum] = i
        
    return ans


arr = [-2, 2, -5, 12, -11, -1, 7]
k = 3

print(longestSubarrayDivK(arr, k))
