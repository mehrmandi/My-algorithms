from bisect import bisect_left

def searchInsertK(arr, k):
    left_index = bisect_left(arr, k)
    return left_index


arr = [1, 3, 5, 6]
k = 2

print(searchInsertK(arr, k))

# [Alternate Approach] Using Binary Search - O(log n) Time and O(1) Space-------------

# def searchInsertK(arr, k):
#     left, right = 0, len(arr) - 1
#     while left < right:
#         mid = left + (right - left) // 2

#         # if arr[mid] is less than k, move to
#         # the right part
#         if arr[mid] < k:
#             left = mid + 1

#         # otherwise, move to the left part
#         else:
#             right = mid

#     # found place: arr[left] is the first element >= k
#     return left + 1 if arr[left] < k else left


# if __name__ == "__main__":
#     arr = [1, 3, 5, 6]
#     k = 5
#     print(searchInsertK(arr, k))
