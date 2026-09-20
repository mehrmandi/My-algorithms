# Given a square matrix mat[][] of size n × n, where each cell contains either 'X' or 'O'. Find the size of the largest square submatrix whose boundary is completely surrounded by 'X'. The cells inside the submatrix can contain either 'X' or 'O'. Only the four sides of the submatrix must contain 'X'.

# Return the side length of the largest such square submatrix.

# Note: A square of size 1 is valid if its only cell is 'X'. If no such square submatrix exists, return 0.

# Precomputing Right and Down X Counts - O(n3) Time and O(n2) Space


def largestSubsquare(mat):
    n = len(mat)
    
    right_traverse = [[0] * n for _ in range(n)]
    down_traverse = [[0] * n for _ in range(n)]
    
    
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if mat[i][j] == "X":
                right_traverse[i][j] = 1 if j == n - 1 else right_traverse[i][j + 1] + 1
                down_traverse[i][j] = 1 if i == n - 1 else down_traverse[i + 1][j] + 1
                           
    res = 0
    
    for i in range(n):
        for j in range(n):
            maxSquere = min(right_traverse[i][j], down_traverse[i][j])
            
            for s in range(maxSquere, 0, -1):
                if right_traverse[i + s - 1][j] >= s and down_traverse[i][j + s - 1] >= s:
                    res = max(res, s)
                    break
                
    return res

mat = [
        ['X', 'X', 'X', 'O'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'O'],
        ['X', 'O', 'X', 'X']
    ]
print(largestSubsquare(mat))
