import bisect
def cntInRange(arr, queries):
    arr.sort()
    res = []
    for q in queries:
        left_idx = bisect.bisect_left(arr, q[0])
        right_idx = bisect.bisect_right(arr, q[1])
        res.append(right_idx - left_idx)
        
    return res
        

arr = [1, 4, 2, 8, 5]
queries = [[1, 4], [3, 6], [0, 10]]
print(cntInRange(arr, queries))

# [Expected Approach] Using Sorting + Binary Search---------------

# def cntInRange(arr, queries):
#     result = []

#     # sort the array once
#     arr.sort()

#     for query in queries:
#         a, b = query[0], query[1]

#         # find the first index where element >= a
#         left = lower_bound(arr, a)

#         # find the first index where element > b
#         right = upper_bound(arr, b)

#         # number of elements in [a, b] is right - left
#         result.append(right - left)

#     return result

# # binary search for first index with element >= target


# def lower_bound(arr, target):
#     low, high = 0, len(arr)
#     while low < high:
#         mid = (low + high) // 2
#         if arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid
#     return low

# # binary search for first index with element > target


# def upper_bound(arr, target):
#     low, high = 0, len(arr)
#     while low < high:
#         mid = (low + high) // 2
#         if arr[mid] <= target:
#             low = mid + 1
#         else:
#             high = mid
#     return low


# if __name__ == "__main__":
#     arr = [1, 4, 2, 8, 5]
#     queries = [[1, 4], [3, 6], [0, 10]]
#     res = cntInRange(arr, queries)
#     for count in res:
#         print(count, end=' ')
#     print()
