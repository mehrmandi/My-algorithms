# Given an array arr[] of positive integers and an integer k, find the total number of pairs of elements that have an absolute difference strictly less than k. Pair (i, j) is considered the same as (j, i).

# Using Sorting with Binary Search - O(n log n) Time and O(1) Space

from bisect import bisect_left

def countPairs(arr: list[int], k: int) -> int:
    n = len(arr)
    res = 0
    arr.sort()
    
    # traverse the array and for each element, find the index of the first element that is greater than or equal to arr[i] + k using binary search. The number of valid pairs for arr[i] will be the difference between this index and i + 1 (to exclude the current element).  
    for i in range(n -1):
        idx = bisect_left(arr, arr[i] + k)
        
        # The number of valid pairs for arr[i] is the difference between idx and i + 1, which gives us the count of elements that are within the range of arr[i] + k. We add this count to the result.
        res += idx - i - 1
        
    return res

arr = [1, 10, 4, 2]
k = 3
print(countPairs(arr, k))
