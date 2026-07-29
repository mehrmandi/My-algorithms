# Problem: Split Array into Minimum Subsets

# Given an array of integers, the task is to split the array into the minimum number of subsets such that each subset contains consecutive integers.

# Hashing - O(n) Time and O(n) Space

def minSubsets(arr):
    # Create a set from the array for O(1) lookups
    arr_set = set(arr)
    res = 0
    
    for num in arr:
        # If num - 1 is not in the set, it means num is the start of a new subset
        if num - 1 not in arr_set:
            res += 1
            
    return res

arr = [100, 56, 5, 6, 102, 58, 101, 57, 7, 103, 59]
print(minSubsets(arr))
    
    