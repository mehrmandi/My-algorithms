# Given an array arr[] representing the fruit values of trees arranged in a circle and an integer m, find the maximum total fruits the bird can collect by visiting at most m trees.

# Bird can start from any tree and move to a neighboring tree.
# The first and last trees are also considered neighbors.
# The bird collects the fruit value of every tree it visits.

# Using Circular Sliding Window - O(n) Time and O(1) Space

def maxFruits(arr: list[int], m: int) -> int:
    n = len(arr)
    sum = 0

    # Calculate the sum of the first m trees.
    for i in range(m):
        sum += arr[i]

    res = sum
    left = 0

    for right in range(m, n + m):
        sum -= arr[left]
        sum += arr[right % n]
        res = max(res, sum)
        left += 1

    return res
        
        
arr = [2, 1, 3, 5, 0, 1, 4]
m = 3
print(maxFruits(arr, m))
