# Given a matrix with n rows and m columns, find the length of the longest path such that:

# The path can start and end at any cell.
# A cell cannot be visited more than once.
# The values in path are strictly increasing.
# From each cell,  you can move left, right, up, or down.
# Diagonal moves and moves outside the matrix are not allowed.

# Using Memoization(DP) + DFS - O(m * n) Time and O(m * n) Space



def longIncPath(matrix, n, m):
     # code here
    dp = [[0 for _ in range(m)] for _ in range(n)]
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfsUtil(i, j):
        if dp[i][j] > 0:
            return dp[i][j]

        dp[i][j] = 1

        for dir in direction:
            newI = i + dir[0]
            newJ = j + dir[1]

            if 0 <= newI < n and 0 <= newJ < m and matrix[newI][newJ] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfsUtil(newI, newJ) + 1)

        return dp[i][j]

    res = 1

    for i in range(n):
        for j in range(m):
            res = max(res, dfsUtil(i, j))

    return res
    
n = 3
m = 3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(longIncPath(matrix, n, m))
