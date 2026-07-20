# def arraySearch(arr, k):
#     if not k in arr:
#         return False

#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = low + (high - low) // 2

#         if low == high:
#             return True

#         elif k in arr[low:mid + 1]:
#             high = mid

#         else:
#             low = mid + 1
            

# def binarySearchMatrix(mat, x):
#     n = len(mat)
#     m = len(mat[0])

#     lo, hi = 0, n * m - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2

#         row = mid // m
#         col = mid % m

#         if mat[row][col] == x:
#             return True

#         if mat[row][col] < x:
#             lo = mid + 1

#         else:
#             hi = mid - 1

#     return False


# def searchMatrix(mat, x):
#     n = len(mat)
#     m = len(mat[0])
   
#     i = 1
    
#     while i < n:
#         if mat[i][0] > mat[i - 1][0]:
#             i += 1   
#         else:
#             break
        

#     before_mat_check = binarySearchMatrix(mat[:i - 1], x) if len(mat[:i - 1]) > 0 else False
#     rotated_arr_check = arraySearch(mat[i - 1], x)
#     after_mat_check = binarySearchMatrix(mat[i:], x) if len(mat[i:]) > 0 else False
    
#     return before_mat_check or rotated_arr_check or after_mat_check    
    
        
# mat = [[39, 42, 45, 4],
#        [7, 10, 14, 19],
#        [22, 26, 29, 34]]

# x = 42

# print(searchMatrix(mat, x))


# 39 42 45 4
# 7 10 14 19
# 22 26 29 34


# [Expected Approach] Binary Search with Index Mapping - O(log(n × m)) Time and O(1) Space--------------------------


def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    low, high = 0, n * m - 1

    while low <= high:
        mid = low + (high - low) // 2

        # convert 1D index to 2D coordinates
        row = mid // m
        col = mid % m
        midVal = mat[row][col]

        # check if mid element is the target
        if midVal == x:
            return True

        # get value at virtual low position
        lowRow = low // m
        lowCol = low % m
        lowVal = mat[lowRow][lowCol]

        # if left half is sorted
        if lowVal <= midVal:

            # check if x lies within the left
            # sorted half
            if lowVal <= x < midVal:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # right half is sorted
            highRow = high // m
            highCol = high % m
            highVal = mat[highRow][highCol]

            # check if x lies within the right
            # sorted half
            if midVal < x <= highVal:
                low = mid + 1
            else:
                high = mid - 1

    # x not found in the matrix
    return False


if __name__ == "__main__":
    mat = [
        [7, 8, 9, 10],
        [11, 12, 13, 1],
        [2, 3, 4, 5]
    ]
    x = 3

    if searchMatrix(mat, x):
        print("true")
    else:
        print("false")
