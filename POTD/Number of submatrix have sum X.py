# def countSquare(mat, x):
#     if not mat or not mat[0]:
#         return 0
    
#     n = len(mat)
#     m = len(mat[0])
#     count = 0
    
#     for left in range(m):
#         temp = [0] * n
        
#         for right in range(left, m):
#             print(left, right)
#             for i in range(n):
#                 temp[i] += mat[i][right]
#                 print(i, temp, temp[i])
                
#             curr_sum = temp[0]
#             for i in range(1, n):
#                 curr_sum = max(temp[i], curr_sum + temp[i])
                
#                 if curr_sum == x:
#                     count += 1
                    
#     return count


# Time Complexity: O(n*m*min(n,m))
# Auxiliary Space: O(n*m)

def countSquare(mat, x):
    res = 0
    n = len(mat)
    m = len(mat[0])

    # Compute row-wise prefix sum
    rowPrefix = [row[:] for row in mat]
    for i in range(n):
        for j in range(1, m):
            rowPrefix[i][j] += rowPrefix[i][j - 1]

    maxSize = min(n, m)

    # Try all possible square sizes
    for size in range(1, maxSize + 1):

        # Try all possible column ranges [i, j] of width 'size'
        for i in range(m - size + 1):
            j = i + size - 1
            total = 0

            # Compute sum for top (size - 1) rows of the square window
            for row in range(size - 1):
                total += rowPrefix[row][j] - \
                    (rowPrefix[row][i - 1] if i > 0 else 0)

            # Slide the square window down row by row
            for row in range(size - 1, n):
                total += rowPrefix[row][j] - \
                    (rowPrefix[row][i - 1] if i > 0 else 0)

                # Check if the current square has sum x
                if total == x:
                    res += 1

                # Remove the top row of the previous window
                total -= rowPrefix[row - size + 1][j] - \
                    (rowPrefix[row - size + 1][i - 1] if i > 0 else 0)

    return res




mat = [[2, 4, 7, 8, 10],
           [3, 1, 1, 1, 1],
           [9, 11, 1, 2, 1],
           [12, -17, 1, 1, 1]]

x = 10

print(countSquare(mat, x))
    