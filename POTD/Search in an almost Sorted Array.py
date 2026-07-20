def searchArray(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        return -1


arr = [-20]
target = -20
print(searchArray(arr, target))


# [Expected Approach] - Using Binary Search - O(log n) Time and O(1) Space


# Bianry search function that returns the
# index of target if found, otherwise -1
# def findTarget(arr, target):
#     l, r = 0, len(arr) - 1

#     while r >= l:
#         mid = l + (r - l) // 2

#         # Check the middle 3 positions
#         if arr[mid] == target:
#             return mid
#         if mid > l and arr[mid - 1] == target:
#             return mid - 1
#         if mid < r and arr[mid + 1] == target:
#             return mid + 1

#         # Search in left subarray
#         if arr[mid] > target:
#             r = mid - 2

#         # Search in right subarray
#         else:
#             l = mid + 2

#     # Element not found
#     return -1


# arr = [10, 3, 40, 20, 50, 80, 70]
# target = 40
# print(findTarget(arr, target))
