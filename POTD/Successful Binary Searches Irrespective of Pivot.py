# Given an array arr[] of n distinct integers(not necessarily sorted), consider the following search for a target:

# Maintain a range[lo, hi], initially[0, n-1].
# At each step, pick any index p in [lo, hi](not necessarily the middle) as pivot. If arr[p] == target, stop - found.
# If target < arr[p], set hi = p - 1
# if target > arr[p], set lo = p + 1. If lo > hi, stop - not found.
# Count the number of indices i such that searching for target = arr[i] succeeds no matter which pivot is chosen at every step(i.e., for every possible sequence of pivot choices).

# Prefix Maximum - O(n) Time and O(n) Space

def countAlwaysFound(arr):
    n = len(arr)

    if n == 0:
        return 0

    # Stores the maximum element from index 0 to i.
    leftMax = [0] * n

    # Initialize the first prefix maximum.
    leftMax[0] = arr[0]

    # Build the prefix maximum array.
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], arr[i])

    # Stores the minimum element seen on the right.
    rightMin = arr[n - 1]
    count = 0

    # The last element is always a candidate because
    # there are no elements on its right.
    if arr[n - 1] == leftMax[n - 1]:
        count += 1

    # Check the remaining elements from right to left.
    for i in range(n - 2, -1, -1):
        # arr[i] must be the maximum of its prefix
        # and smaller than every element on its right.
        if arr[i] == leftMax[i] and arr[i] < rightMin:
            count += 1

        # Update the minimum element seen on the right.
        rightMin = min(rightMin, arr[i])

    return count
    

arr = [3, 7, 9, 8, 15]
print(countAlwaysFound(arr))
