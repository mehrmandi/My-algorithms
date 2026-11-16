# Given an array arr[] of distinct positive integers and a positive integer k. Consider an infinite sequence of natural numbers starting from 1. The task is to remove all elements present in arr[] from this sequence.

# Find the k-th smallest number in the remaining sequence.

# Note: Your solution must run in O(1) auxiliary space.

# Sorting - O(n log n) Time and O(1) Space

def findKthSmall(arr, k):
    # Sort the array in ascending order
    arr.sort()

    # Update k based on removed numbers
    for num in arr:
        # Shift k forward if the number is removed
        if num <= k:
            k += 1
        else:
            break

    # Return the k-th missing number
    return k


arr = [11, 1, 16, 19]
k = 11
print(findKthSmall(arr, k))
    