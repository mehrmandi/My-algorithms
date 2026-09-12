# Given an array arr[] of integers and an integer k, find a subsequence of size k whose product is maximum among all possible subsequences of size k. Return the maximum product that can be obtained.

# Greedy Approach Using Sorting - O(n log n) Time and O(1) Space


def maxProduct(arr: list[int], k: int) -> int:
    n = len(arr)
    arr.sort()
    
    # Store the maximum product.
    res = 1
    
    # If the largest element is 0 and k is odd.
    if arr[n - 1] == 0 and (k & 1):
        return 0
    
    # If all elements are non-positive and k is odd.
    if arr[n - 1] < 0 and (k & 1):
        for i in range(n - 1, n - k - 1, -1):
            res *= arr[i]
            
        return res
    
    l, r = 0, n - 1
    
    # Include the largest positive element if k is odd.
    if k & 1:
        res *= arr[r]
        r -= 1
        k -= 1
    
    # Process remaining elements in pairs
    k = k // 2
    
    for i in range(k):
        r_pro = arr[r] * arr[r - 1]
        l_pro = arr[l] * arr[l + 1]
        
        if r_pro > l_pro:
            res *= r_pro
            r -= 2
            
        else:
            res *= l_pro
            l += 2
    
    return res
    
    

arr = [1, 2, -1, -3, -6, 4]
k = 4
print(maxProduct(arr, k))
