import heapq

# [Expected Approach] – Using Priority Queue – O(n^2 * log(k)) Time and O(k) Space------------------------------------
def kthElementMatrix(matrix, k):
    n = len(matrix)
    pq = []
    
    for i in range(n):
        for j in range(n):
            if len(pq) < k:
                heapq.heappush(pq, -matrix[i][j])
                
            elif matrix[i][j] <= -pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, -matrix[i][j])
    
    
   
    return -pq[0]
    


# n = 4
mat = [[16, 28, 60, 64], 
       [22, 41, 63, 91], 
       [27, 50, 87, 93], 
       [36, 78, 87, 94]]
k = 7

# mat = [[10, 20, 30, 40], 
#        [15, 25, 35, 45], 
#        [24, 29, 37, 48], 
#        [32, 33, 39, 50]]


print(kthElementMatrix(mat, k))


# [Expected Approach for Small Range] – Binary Search on Range – O(n* log(max-min)) Time and O(1) Space--------------------------------------

# Python program to find the Kth smallest element

# Function to count the number of elements less than or equal to x
# def countSmallerEqual(matrix, x):
#     n = len(matrix)
#     count = 0
#     row = 0
#     col = n - 1

#     # Traverse from the top-right corner
#     while row < n and col >= 0:
#         if matrix[row][col] <= x:

#             # If current element is less than
#             # or equal to x, all elements in this
#             # row up to the current column are <= x
#             count += (col + 1)
#             row += 1
#         else:

#             # Move left in the matrix
#             col -= 1

#     return count

# # Function to find the kth smallest
# # element in a sorted 2D matrix


# def kthSmallest(matrix, k):
#     n = len(matrix)
#     low = matrix[0][0]
#     high = matrix[n - 1][n - 1]
#     ans = 0

#     while low <= high:
#         mid = low + (high - low) // 2

#         # Count elements less than or equal to mid
#         count = countSmallerEqual(matrix, mid)

#         if count < k:

#             # If there are less than k elements
#             # <= mid, the kth smallest is larger
#             low = mid + 1
#         else:

#             # Otherwise, mid might be the answer,
#             # but we need to check for smaller values
#             ans = mid
#             high = mid - 1

#     return ans


# if __name__ == "__main__":
#     matrix = [
#         [10, 20, 30, 40],
#         [15, 25, 35, 45],
#         [24, 29, 37, 48],
#         [32, 33, 39, 50]]
#     k = 3
#     result = kthSmallest(matrix, k)

#     print(result)
