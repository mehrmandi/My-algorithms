# from collections import deque

# def countUniquePath(grid):
#     n = len(grid)
#     m = len(grid[0])
#     counter = 0
#     dirr = [[1, 0], [0, 1]]
    
#     if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
#         return counter
    
#     if m == 1 and n == 1:
#         return 1
    
#     q = deque([(0, 0)])
    
#     while q:
#         sz = len(q)
        
#         for i in range(sz):
#             curr = q.popleft()
#             x , y = curr
            
#             for j in range(2):
#                 new_x = x + dirr[j][0]
#                 new_y = y + dirr[j][1]
                
#                 if new_x == n - 1 and new_y == m - 1:
#                     counter += 1
                    
#                 elif new_x >= 0 and new_y >= 0 and new_x < n and new_y < m:
#                     if grid[new_x][new_y] == 0:
#                         q.append((new_x, new_y))
                        
#     return counter


# grid = [[0]]
# print(countUniquePath(grid))

# Using Space Optimized DP – O(m*n) Time and O(n * m) Space-----------------------------------
def countUniquePaths(grid):
    n = len(grid)
    m = len(grid[0])

    # If start or end is blocked, no valid path exists.
    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return 0

    # Initialize the dp table with zeros.
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1  # Starting position

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 0  # Obstacle cell, skip updating
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    return dp[n - 1][m - 1]


# Example usage:
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(countUniquePaths(grid))  # Output: 2

# Using Space Optimized DP – O(m*n) Time and O(n) Space--------------------------------------
# Python code to find number of unique paths
# using Space-Optimized Tabulation

# Function to find unique paths with obstacles
# def uniquePaths(grid):
#     n = len(grid)
#     m = len(grid[0])

#     # If starting or ending cell is an obstacle, return 0
#     if grid[0][0] == 1 or grid[n-1][m-1] == 1:
#         return 0

#     # Initialize dp array with 0
#     dp = [0] * m

#     # Set the value for the bottom-right cell
#     dp[m-1] = 1

#     # Fill the bottom row first
#     for j in range(m-2, -1, -1):

#         # As this is an obstacle, no paths will
#         # exist from this cell.
#         if grid[n-1][j] == 1:
#             dp[j] = 0

#         # Otherwise, a straight path to
#         # n-1, m-1 exists
#         else:
#             dp[j] = dp[j+1]

#     # Process each row from bottom to top
#     for i in range(n-2, -1, -1):

#         # Process the rightmost column of the current row
#         if grid[i][m-1] == 1:
#             dp[m-1] = 0

#         # Process each cell from right to left
#         for j in range(m-2, -1, -1):

#             # If current cell is an obstacle, paths = 0
#             if grid[i][j] == 1:
#                 dp[j] = 0

#             # Otherwise, paths = sum of right and down paths
#             else:
#                 dp[j] = dp[j] + dp[j+1]

#     return dp[0]


# if __name__ == "__main__":
#     grid = [
#         [0, 0, 0],
#         [0, 1, 0],
#         [0, 0, 0]
#     ]

#     print(uniquePaths(grid))
