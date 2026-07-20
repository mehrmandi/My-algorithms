# import numpy as np
# def transpose(mat):
#     np_mat = np.array(mat)
    
#     return np_mat.T

# mat = [[1, 1, 1, 1],
#                  [2, 2, 2, 2],
#                  [3, 3, 3, 3],
#                  [4, 4, 4, 4]]

# print(transpose(mat))
# [Approach 2] Using constant space for Square Matrix O(n*n) Time and O(1) Space-----------



def transpose(mat):

    # Number of rows (and columns, since it's square)
    n = len(mat)

    # Traverse the upper triangle of the matrix
    for i in range(n):
        for j in range(i + 1, n):

            # Swap elements across the diagonal
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    return mat


if __name__ == "__main__":
    mat = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    res = transpose(mat)
    for row in res:
        print(" ".join(map(str, row)))
