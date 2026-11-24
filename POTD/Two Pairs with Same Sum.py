
# Given an array arr[] of positive integers, find four indices a, b, c, and d such that arr[a] + arr[b] = arr[c] + arr[d], where a, b, c, d are all distinct indices.

# If multiple such quadruplets exist, return the one that is lexicographically smallest when the indices are considered in the order a, b, c, d.
# If no such quadruplet exists, return {-1, -1, -1, -1}. 
# Ensure a < b and c < d, and the pair (a, b) is lexicographically smaller than the pair (c, d).

# Hashing Pair Sums - O(n ^ 2) Time and O(n ^ 2) Space


def findPairs(arr: list[int]) -> list[int]:
    n = len(arr)
    hash = {}
    res = None
    
    for i in range(n):
        for j in range(i + 1, n):
            curr_sum = arr[i] + arr[j]
            
            if curr_sum not in hash:
                hash[curr_sum] = [i, j]
                continue
            
            a, b = hash[curr_sum]
            
            if a == i or b == i or a == j or b == j:
                continue
            
            curr_res = [a, b, i, j]
            
            if not res or curr_res < res:
                res = curr_res
                
    
    if not res:
        return [-1, -1, -1, -1]
    
    return res
    



arr = [3, 4, 7, 1, 2, 9, 8]
print(findPairs(arr))

    
    
    
