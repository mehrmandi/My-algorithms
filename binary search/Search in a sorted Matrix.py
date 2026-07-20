def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    lo, hi = 0, n * m - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        # Find row and column of element at mid index
        row = mid // m
        col = mid % m

        # If x is found, return true
        if mat[row][col] == x:
            return True

        # If x is greater than mat[row][col], search in
        # right half
        if mat[row][col] < x:
            lo = mid + 1

        # If x is less than mat[row][col], search in
        # left half
        else:
            hi = mid - 1

    return False

if __name__ == "__main__":
    mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    x = 14

    if searchMatrix(mat, x):
        print("true")
    else:
        print("false")








# def matrix_search(arr, k):
#     n = len(arr[0])
#     m = len(arr)
#     i = 0
#     j = 0
#
#     while 0 <= i < m and 0 <= j < n:
#         if arr[i][j] == k:
#             return True
#
#         elif k < arr[i][j]:
#             if j > 0:
#                 j -= 1
#             else:
#                 i += 1
#
#         else:
#             if j < n - 1:
#                 j += 1
#             else:
#                 i += 1
#
#     return False
#
#
# arr = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
# k = 20
#
# print(matrix_search(arr, k))