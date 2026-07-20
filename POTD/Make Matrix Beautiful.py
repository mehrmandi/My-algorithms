# import numpy as np

# def balanceSums(mat):
#     n =  len(mat)
#     mat = np.array(mat)
#     reversed_mat = mat.T
#     max_sum_row= 0
#     mat_sum = 0 
#     max_sum_col = 0
    
    
#     for i in range(n):
#         row_sum = sum(mat[i])
#         col_sum = sum(reversed_mat[i])
#         max_sum_row = max(max_sum_row, row_sum)
#         mat_sum += row_sum
#         max_sum_col = max(max_sum_col, col_sum)
  
        
#     res_row = (max_sum_row * n) - mat_sum
#     res_col = (max_sum_col * n) - mat_sum
        
#     return max(res_col, res_row)


# mat = [
#     [1, 2, 3, 12, 15, 5],
#     [4, 2, 3, 10, 10, 2],
#     [3, 2, 1, 14, 12, 6],
#     [1, 2, 3, 12, 15, 5],
#     [4, 2, 3, 10, 10, 2],
#     [3, 2, 1, 14, 12, 6]]
# print(balanceSums(mat))


# [Expected Approach] Max-Target Normalization - O(n^2) Time and O(1) Time----------------------------

def balanceSum(mat):
    n = len(mat)
    res = 0
    maxSum = 0

    # Find maximum sum across all rows
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += mat[i][j]
        maxSum = max(sum, maxSum)

    # Find maximum sum across all columns
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += mat[i][j]
        maxSum = max(sum, maxSum)

    # Sum of operations across all rows
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += mat[i][j]
        res += (maxSum - sum)

    return res


if __name__ == "__main__":
    mat = [
        [1, 2, 3, 12, 15, 5],
        [4, 2, 3, 10, 10, 2],
        [3, 2, 1, 14, 12, 6],
        [1, 2, 3, 12, 15, 5],
        [4, 2, 3, 10, 10, 2],
        [3, 2, 1, 14, 12, 6]]
    print(balanceSum(mat))

