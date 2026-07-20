# Two-Pointer Diagonal Swap - O(n) Time and O(1) Time------------------


def swapDiagonal(mat):
    n = len(mat)
    
    for i in range(n):
        mat[i][i], mat[i][n - 1 - i] = mat[i][n - 1 - i], mat[i][i]
        
    return mat


mat = [[0, 1, 2, 3],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
print(swapDiagonal(mat))