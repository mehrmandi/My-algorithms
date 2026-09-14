# Given a 2D binary matrix mat[][] where 0 represents a landmine and 1 represents a safe cell, find the length of the shortest safe route from any cell in the first column to any cell in the last column.

# You can move only up, down, left, or right, and can enter only safe cells(cells that are neither landmines nor adjacent to a landmine). If there is no safe path to reach the last column, return -1.


# Using Breadth First Search - O(n*m) Time and O(n*m) Space

from collections import deque

def isSafe(mat, r, c, visited,rows, cols):
    return (0 <= r < rows) and (0 <= c < cols) and (not visited[r][c]) and (mat[r][c] == 1 
     and (r + 1 == rows or mat[r + 1][c] == 1) and (c + 1 == cols or mat[r][c + 1] == 1)
     and (c == 0 or mat[r][c - 1] == 1) and (r == 0 or mat[r - 1][c] == 1))
    


def shortestPath(mat: list[list[int]]) -> int:
    rows = len(mat)
    cols = len(mat[0])
    
    dirrections = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    q = deque([])
    
    for i in range(rows):
        if isSafe(mat, i, 0, visited, rows, cols):
            q.append([i, 0, 1])
            visited[i][0] = True
            
    while q:
        r, c, step = q.popleft()
        if c == cols - 1:
            return step
        
        for dir in dirrections:
            newr = r + dir[0]
            newc = c + dir[1]
            
            if isSafe(mat, newr, newc, visited, rows, cols):
                q.append([newr, newc, step + 1])
                visited[newr][newc] = True
                    
    return -1
            
    
mat = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]
print(shortestPath(mat))