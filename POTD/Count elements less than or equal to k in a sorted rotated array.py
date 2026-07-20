import bisect

def countLessEqual(arr, x):
    n = len(arr)
    rotate_idx = 0
    
    
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            rotate_idx = i
    
    
    right_idx = bisect.bisect_right(arr, x, rotate_idx, n) - rotate_idx
    left_idx = bisect.bisect_right(arr, x, 0, rotate_idx)

    return right_idx + left_idx


arr = [6, 10, 12, 15, 2, 4, 5]
x = 14
print(countLessEqual(arr, x))


# [Expected Approach] Using Binary Search - O(log(n)) Time and O(1) Space----------------

# Standard binary search to count
# elements ≤ x in a sorted subarray
# def countInSorted(arr, left, right, x):
#     l, r = left, right
#     res = left - 1
#     while l <= r:
#         mid = l + (r - l) // 2
#         if arr[mid] <= x:
#             res = mid
#             l = mid + 1
#         else:
#             r = mid - 1
#     return res - left + 1


# Function to find index of the smallest
# element (pivot) in rotated array


# def findPivot(arr):
#     n = len(arr)
#     l, r = 0, n - 1
#     while l < r:
#         mid = l + (r - l) // 2
#         if arr[mid] > arr[r]:
#             l = mid + 1
#         else:
#             r = mid
#     # index of the smallest element
#     return l

# # Main function to count elements ≤ x in a rotated sorted array


# def countLessEqual(arr, x):
#     n = len(arr)
#     pivot = findPivot(arr)

#     # Search in both sorted parts
#     count1 = countInSorted(arr, 0, pivot - 1, x)
#     count2 = countInSorted(arr, pivot, n - 1, x)

#     return count1 + count2


# arr = [6, 10, 12, 15, 2, 4, 5]
# x = 14

# print(countLessEqual(arr, x))
