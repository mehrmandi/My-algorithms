# [Expected Approach] - O(log n) Time and O(1) Space-------------------

def findKRotation(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:

        # If subarray is already sorted,
        # smallest is at low
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2

        # Minimum is in the right half
        if arr[mid] > arr[high]:
            low = mid + 1

        # Minimum is in the left half (could be mid)
        else:
            high = mid

    return low
