# Given an array arr[], find the minimum sum of a subarray containing atleast one element in the given array.

# Using Kadane's Algorithm - O(n) Time and O(1) Space

def minSubarraySum(arr: list[int]) -> int:
    n = len(arr)
    res = arr[0]

    minEnding = arr[0]

    for i in range(1, n):
        minEnding = min(minEnding + arr[i], arr[i])

        res = min(res, minEnding)

    return res


arr = [2, 6, 8, 1, 4]
print(minSubarraySum(arr))
    
        
