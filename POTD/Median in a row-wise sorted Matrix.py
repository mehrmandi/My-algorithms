# def is_potential_median(mat, mid, n, m):
#     count = 0
#     for i in range(n * m):
#         row = i // m
#         col = i % m
#         if mat[row][col] <= mid:
#             count += 1
#     return count


# def median(mat):
#     n = len(mat)
#     m = len(mat[0])
    
#     median_index = (n * m) // 2
#     min_val = min(min(mat))
#     max_val = max(max(mat))
#     res = 0
#     print(median_index)
    
#     low, high = min_val, max_val
    
#     while low <= high:
#         mid = (low + high) // 2
        
        
#         count = is_potential_median(mat, mid, n, m)
#         print(low, high, mid, count)
        
        
#         if count <= median_index:
#             low = mid + 1
            
#         elif count > median_index:
#             high = mid
            
#     print("low, high", low, high)
#     res = low
    
        
#     return res
            

# mat = [[4, 7, 10, 11, 15, 39, 50],
#        [1, 2, 3, 4, 6, 7, 8],
#        [3, 5, 7, 10, 12, 15, 20]]

# print(median(mat))

# arr = [4, 7, 10, 11, 15, 39, 50, 1, 2, 3, 4, 6, 7, 8, 3, 5, 7, 10, 12, 15, 20]
# arr.sort()
# print(arr, arr[10])

# ime Complexity: O(n × log(m) × log(maxVal - minVal)), the upper bound function will take log(m) time and is performed for each row. And binary search is performed from minVal to maxVal.
# Auxiliary Space: O(1)



from bisect import bisect_right


def median(mat):
    n = len(mat)
    m = len(mat[0])

    minVal = float('inf')
    maxVal = float('-inf')

    # finding the minimum and maximum elements
    # in the matrix
    for i in range(n):
        minVal = min(minVal, mat[i][0])
        maxVal = max(maxVal, mat[i][m - 1])

    desired = (n * m + 1) // 2
    lo = minVal
    hi = maxVal

    # binary search to find the median
    while lo < hi:
        mid = lo + (hi - lo) // 2
        place = 0

        # count elements smaller than or equal to mid
        # using bisect_right
        for i in range(n):
            place += bisect_right(mat[i], mid)

        if place < desired:
            lo = mid + 1
        else:
            hi = mid

    return lo


if __name__ == "__main__":
    mat = [[1, 3, 5],
           [2, 6, 9],
           [3, 6, 9]]
    print(median(mat))
    