# from collections import deque

# def minCostPath(mat):
#     n = len(mat)
#     m = len(mat[0])
    
#     direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     min_cost = [[float('inf') for _ in range(m)] for _ in range(n)]
    
#     q = deque()
#     q.append([0, 0, 0])
#     visited[0][0] = True
#     min_cost[0][0] = 0
    
    
#     while q:
#         sz = len(q)
        
#         for i in range(sz):
#             x, y, min_val = q.popleft()
#             min_prev = min_cost[x][y]
            
#             for dir in direction:
#                 newX = x + dir[0]
#                 newY = y + dir[1]
                
                
#                 if 0 <= newX < n and 0 <= newY < m:
#                     min_until = max(min_prev, abs(mat[newX][newY] - mat[x][y]))
                    
#                     if not visited[newX][newY]:
#                         visited[newX][newY] = True
#                         q.append([newX, newY, min_cost[newX][newY]])
                        
#                     if min_until < min_cost[newX][newY]:
#                         min_cost[newX][newY] = min_until
#                         q.append([newX, newY, min_cost[newX][newY]])                   
                        
#     return min_cost[n - 1][m - 1]


# mat = [[2, 2, 2, 1],
#        [8, 1, 2, 7],
#        [2, 2, 2, 8],
#        [2, 1, 4, 7],
#        [2, 2, 2, 2]]

# print(minCostPath(mat))


# [Expected Approach - 2] - Using DSU - O((n*m) log(n*m)) Time and O(n*m) Space--------------------
# DSU class
# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0]*n

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def unite(self, x, y):
#         px, py = self.find(x), self.find(y)
#         if px == py:
#             return
#         if self.rank[px] < self.rank[py]:
#             self.parent[px] = py
#         elif self.rank[px] > self.rank[py]:
#             self.parent[py] = px
#         else:
#             self.parent[py] = px
#             self.rank[px] += 1

#     def connected(self, x, y):
#         return self.find(x) == self.find(y)


# def minCostPath(mat):
#     n, m = len(mat), len(mat[0])
#     total = n*m

#     # Store edges: (weight, cell1, cell2)
#     edges = []
#     for i in range(n):
#         for j in range(m):
#             u = i*m+j
#             # Only right and down neighbors
#             if i+1 < n:
#                 edges.append([abs(mat[i][j]-mat[i+1][j]), u, (i+1)*m+j])
#             if j+1 < m:
#                 edges.append([abs(mat[i][j]-mat[i][j+1]), u, i*m+j+1])

#     # Sort edges by weight
#     edges.sort()

#     dsu = DSU(total)

#     # Connect cells using edges in increasing order
#     for w, u, v in edges:
#         dsu.unite(u, v)

#         # Check if start and end are connected
#         if dsu.connected(0, total-1):
#             return w

#     # Single cell case
#     return 0


# if __name__ == '__main__':
#     mat = [[2, 2, 2, 1],
#            [8, 1, 2, 7],
#            [2, 2, 2, 8],
#            [2, 1, 4, 7],
#            [2, 2, 2, 2]]
#     print(minCostPath(mat))




# [Expected Approach - 1] - Using Dijkstra's Algorithm------------------------------------------

import heapq

# Directions: up, down, left, right
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def minCostPath(mat):
    n, m = len(mat), len(mat[0])
    cost = [[float('inf')]*m for _ in range(n)]
    cost[0][0] = 0

    # {current cost, x, y}
    pq = [(0, 0, 0)]
    while pq:
        currCost, x, y = heapq.heappop(pq)

        # Skip if this is an outdated entry
        if currCost != cost[x][y]:
            continue

        # Destination reached
        if x == n-1 and y == m-1:
            return currCost

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:

                # Maximum difference along this path
                newCost = max(currCost, abs(mat[nx][ny] - mat[x][y]))

                # Update if newCost improves the neighbor
                if newCost < cost[nx][ny]:
                    cost[nx][ny] = newCost
                    heapq.heappush(pq, (newCost, nx, ny))

    return cost[n-1][m-1]


if __name__ == '__main__':
    mat = [
        [7, 2, 6, 5],
        [3, 1, 10, 8]
    ]
    print(minCostPath(mat))
