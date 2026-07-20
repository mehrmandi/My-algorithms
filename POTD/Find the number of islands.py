from collections import deque

def BFS(grid, visited, islands, i, j, row, col):
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
    islands[0] += 1
    sub_q = deque()
    sub_q.append([i, j])
    while sub_q:
        sz = len(sub_q)
        for i in range(sz):
            curr = sub_q.popleft()
            x, y = curr

            for d0, d1 in direction:
                newX, newY = x + d0, y + d1

                if 0 <= newX < row and 0 <= newY < col and not visited[newX][newY]:
                    if grid[newX][newY] == "L":
                        sub_q .append([newX, newY])
                        visited[newX][newY] = True
                        


def countIsland(grid):
    row, col = len(grid), len(grid[0])
    visited = [[False for _ in range(col)] for _ in range(row)]
    q = deque()
    islands = [0]

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "L":
                q.append([i, j])

    while q:
        sz = len(q)

        for i in range(sz):
            curr = q.popleft()
            x, y = curr

            if not visited[x][y]:
                BFS(grid, visited, islands, x, y, row, col)

    return islands[0]


grid = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]

print(countIsland(grid))

# L W L L
# W L W L
# L L W L
# W W L L
# L L L L


#  Using Breadth First Search - O(n*m) time and O(n*m) space----------------------------------------------------------
# from collections import deque
#
# # A function to check if a given cell (r, c) can be included in BFS
# def isSafe(grid, r, c, vis):
#     rows = len(grid)
#     cols = len(grid[0])
#     return (0 <= r < rows) and (0 <= c < cols) and (grid[r][c] == 'L' and not vis[r][c])
#
# # Breadth-First-Search to visit all cells in the current island
# def bfs(grid, vis, sr, sc):
#     # These arrays are used to get row and column numbers of 8 neighbors
#     rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
#     cNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
#
#     # Simple BFS first step, we enqueue source and mark it as visited
#     q = deque([(sr, sc)])
#     vis[sr][sc] = True
#
#     # Process all items in the queue
#     while q:
#         r, c = q.popleft()
#
#         # Explore all 8 adjacent cells
#         for k in range(8):
#             newR = r + rNbr[k]
#             newC = c + cNbr[k]
#             if isSafe(grid, newR, newC, vis):
#                 vis[newR][newC] = True
#                 q.append((newR, newC))
#
# # This function returns the number of islands (connected components) in a grid
# def countIslands(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     vis = [[False] * cols for _ in range(rows)]
#
#     island_count = 0  # Island count
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'L' and not vis[r][c]:
#                 bfs(grid, vis, r, c)
#                 island_count += 1
#
#     return island_count
#
# # Driver Code
# if __name__ == "__main__":
#     grid = [
#         ['L', 'L', 'W', 'W', 'W'],
#         ['W', 'L', 'W', 'W', 'L'],
#         ['L', 'W', 'W', 'L', 'L'],
#         ['W', 'W', 'W', 'W', 'W'],
#         ['L', 'W', 'L', 'L', 'W']
#     ]
#
#     print(countIslands(grid))


# Using Disjoint Set - O(n*m) time and O(n*m) space-------------------------------------------------------------
# class DisjointSet:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])  # Path compression
#         return self.parent[x]
#
#     def union(self, x, y):
#         xroot = self.find(x)
#         yroot = self.find(y)
#         if xroot == yroot:
#             return
#         if self.rank[xroot] < self.rank[yroot]:
#             self.parent[xroot] = yroot
#         elif self.rank[yroot] < self.rank[xroot]:
#             self.parent[yroot] = xroot
#         else:
#             self.parent[yroot] = xroot
#             self.rank[xroot] += 1
#
# def countIslands(grid):
#     if not grid:
#         return 0
#
#     rows, cols = len(grid), len(grid[0])
#     ds = DisjointSet(rows * cols)
#
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
#                   (-1, -1), (-1, 1), (1, -1), (1, 1)]
#
#     def index(r, c):
#         return r * cols + c
#
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'L':
#                 for dr, dc in directions:
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'L':
#                         ds.union(index(r, c), index(nr, nc))
#
#     unique_islands = set()
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'L':
#                 root = ds.find(index(r, c))
#                 unique_islands.add(root)
#
#     return len(unique_islands)
#
# # Driver
# grid = [
#     ['L', 'L', 'W', 'W', 'W'],
#     ['W', 'L', 'W', 'W', 'L'],
#     ['L', 'W', 'W', 'L', 'L'],
#     ['W', 'W', 'W', 'W', 'W'],
#     ['L', 'W', 'L', 'L', 'W']
# ]
#
# print( countIslands(grid))



# ---------------------------------------------------
# from collections import deque
#
#
# # A function to check if a given cell (r, c) can be included in BFS
# def isSafe(grid, r, c):
#     rows, cols = len(grid), len(grid[0])
#     return (0 <= r < rows) and (0 <= c < cols) and (grid[r][c] == 'L')
#
#
# # Breadth-First-Search to visit all cells in the current island
# def bfs(grid, sr, sc):
#     # These arrays are used to get row and column numbers of 8 neighbors
#     rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
#     cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
#
#     # Simple BFS first step, enqueue source and mark it as visited
#     q = deque([(sr, sc)])
#     grid[sr][sc] = 'W'  # Mark as visited by changing 'L' to 'W'
#
#     # Process all items in the queue
#     while q:
#         r, c = q.popleft()
#
#         # Explore all 8 adjacent cells
#         for k in range(8):
#             newR, newC = r + rNbr[k], c + cNbr[k]
#             if isSafe(grid, newR, newC):
#                 grid[newR][newC] = 'W'  # Mark as visited
#                 q.append((newR, newC))
#
#
# # This function returns the number of islands (connected components) in a grid
# def countIslands(grid):
#     rows, cols = len(grid), len(grid[0])
#     islandCount = 0
#
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'L':
#                 bfs(grid, r, c)
#                 islandCount += 1
#
#     return islandCount
#
#
# if __name__ == "__main__":
#     grid = [
#         ['L', 'L', 'W', 'W', 'W'],
#         ['W', 'L', 'W', 'W', 'L'],
#         ['L', 'W', 'W', 'L', 'L'],
#         ['W', 'W', 'W', 'W', 'W'],
#         ['L', 'W', 'L', 'L', 'W']
#     ]
#
#     print(countIslands(grid))

# Using DFS and Additional Matrix - O(n*m) Time and O(n*m) Space----------------------------------------------------------------
#
# def isSafe(grid, r, c, visited):
#     row = len(grid)
#     col = len(grid[0])
#
#     return (0 <= r < row) and (0 <= c < col) and (grid[r][c] == 'L' and not visited[r][c])
#
#
# def dfs(grid, r, c, visited):
#     rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
#     cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
#
#     # Mark this cell as visited
#     visited[r][c] = True
#
#     # Recur for all connected neighbours
#     for k in range(8):
#         newR, newC = r + rNbr[k], c + cNbr[k]
#         if isSafe(grid, newR, newC, visited):
#             dfs(grid, newR, newC, visited)
#
#
# def countIslands(grid):
#     row = len(grid)
#     col = len(grid[0])
#
#     visited = [[False for _ in range(col)] for _ in range(row)]
#
#     count = 0
#     for r in range(row):
#         for c in range(col):
#
#             # If a cell with value 'L' (land) is not visited yet,
#             # then a new island is found
#             if grid[r][c] == 'L' and not visited[r][c]:
#                 # Visit all cells in this island.
#                 dfs(grid, r, c, visited)
#
#                 # increment the island count
#                 count += 1
#     return count
#
#
# if __name__ == "__main__":
#     grid = [
#         ['L', 'L', 'W', 'W', 'W'],
#         ['W', 'L', 'W', 'W', 'L'],
#         ['L', 'W', 'W', 'L', 'L'],
#         ['W', 'W', 'W', 'W', 'W'],
#         ['L', 'W', 'L', 'L', 'W']
#     ]
#
#     print(countIslands(grid))


# [Approach 2] Using Space Optimized DFS - O(n*m) Time and O(1) Space ----------------------------------------------------------
# A function to check if a given
# cell (r, c) can be included in DFS
# def isSafe(grid, r, c):
#     row = len(grid)
#     col = len(grid[0])
#
#     # r is in range, c is in range, value
#     # is 'L' (land)
#     return (0 <= r < row) and (0 <= c < col) and grid[r][c] == 'L'
#
# # A utility function to do DFS for a
# # 2D matrix. It only considers
# # the 8 neighbors as adjacent vertices
# def dfs(grid, r, c):
#     # These arrays are used to get
#     # r and c numbers of 8
#     # neighbours of a given cell
#     rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
#     cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
#
#     # Mark this cell as visited
#     grid[r][c] = 'W'
#
#     # Recur for all connected neighbours
#     for k in range(8):
#         newR = r + rNbr[k]
#         newC = c + cNbr[k]
#         if isSafe(grid, newR, newC):
#             dfs(grid, newR, newC)
#
# # The main function that returns
# # count of islands in a given matrix
# def countIslands(grid):
#     row = len(grid)
#     col = len(grid[0])
#
#     count = 0
#     for r in range(row):
#         for c in range(col):
#             if grid[r][c] == 'L':
#                 dfs(grid, r, c)
#                 count += 1
#     return count
#
# # Main execution
# if __name__ == "__main__":
#     grid = [
#         ['L', 'L', 'W', 'W', 'W'],
#         ['W', 'L', 'W', 'W', 'L'],
#         ['L', 'W', 'W', 'L', 'L'],
#         ['W', 'W', 'W', 'W', 'W'],
#         ['L', 'W', 'L', 'L', 'W']
#     ]
#     print(countIslands(grid))  # Expected output: 4
#
