# Given a square chessboard of size n × n, the initial position knightPos and target position targetPos of a Knight are given. Find the minimum number of moves required for the Knight to reach targetPos.

# A Knight moves in an L-shape, covering 2 cells in one direction and 1 cell perpendicular to it. From(x, y), it can move to: (x ± 2, y ± 1) and (x ± 1, y ± 2)

# This gives at most 8 possible moves:
# Note: The positions are given using 1-based indexing.


# BFS - Shortest Path in O(n ^ 2) Time and O(n ^ 2) Space

from collections import deque

def minStepToReachTarget(knightPos: list[int], targetPos: list[int], n: int) -> int:
    q = deque([[knightPos[0], knightPos[1], 0]])
    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    visited[knightPos[0]][knightPos[1]] = True
    directions = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, -2], [1, 2], [-1, -2], [-1, 2]]
    
    while q:
        x, y, m = q.popleft()
        print(x, y, m)
        
        if [x, y] == targetPos:
            return m
        
        for dir in directions:
            nX = x + dir[0]
            nY = y + dir[1]
            print(nX, nY)
            
            if 0 < nX <= n and 0 < nY <= n and not visited[nX][nY]:
                q.append([nX, nY, m + 1])
                visited[nX][nY] = True
            
    


n = 3
knightPos= [3, 3]
targetPos= [1, 2]
print(minStepToReachTarget(knightPos, targetPos, n))
