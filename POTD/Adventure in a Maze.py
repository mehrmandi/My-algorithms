# Given a maze represented as an n x n grid, grid[][], using 0-based indexing. Each cell contains one of the values 1, 2, or 3, which determines the direction(s) you are allowed to move from that cell:

# 1 - you may move Right only.
# 2 - you may move Down only.
# 3 - you may move Right or Down(both directions are available).
# You start at the top-left cell(0, 0)(the Entry) and must reach the bottom-right cell(n-1, n-1)(the Exit), following the movement rule of each cell you pass through. You are never allowed to move outside the boundaries of the grid.

# The Adventure of a path is the sum of the values of all cells visited along that path(including both the entry and exit cells).

# Find the total number of distinct valid paths from Entry to Exit, and among all such paths, the maximum possible Adventure. Return the answer as [totalPaths, maxAdventure].

# Note: Return totalPaths modulo 109 + 7, maxAdventure needs no modulo, as it stays small regardless of grid size.


#  Using Bottom-Up DP - O(n ^ 2) Time and O(n) Space

def findWays(grid):
    MOD = 10**9 + 7
    n = len(grid)

    # Arrays to store the data of the "next" row below (i + 1)
    nextWays = [0] * n

    # Initialize as unreachable (-1)
    nextAdv = [-1] * n

    # Iterate backwards from the bottom row to the top row
    for i in range(n - 1, -1, -1):
        currWays = [0] * n
        currAdv = [-1] * n

        for j in range(n - 1, -1, -1):
            # Base Case: Bottom-right cell (The Exit)
            if i == n - 1 and j == n - 1:
                currWays[j] = 1
                currAdv[j] = grid[i][j]
                continue

            totalWays = 0
            maxAdventure = -1
            cellValue = grid[i][j]

            # Option 1: Move Right (Valid for cell values 1 and 3)
            if cellValue == 1 or cellValue == 3:
                # Check if right neighbor is within boundaries and reachable
                if j + 1 < n and currAdv[j + 1] != -1:
                    totalWays = (totalWays + currWays[j + 1]) % MOD
                    maxAdventure = max(
                        maxAdventure, grid[i][j] + currAdv[j + 1])

            # Option 2: Move Down (Valid for cell values 2 and 3)
            if cellValue == 2 or cellValue == 3:
                # Check if bottom neighbor is within boundaries and reachable
                if i + 1 < n and nextAdv[j] != -1:
                    totalWays = (totalWays + nextWays[j]) % MOD
                    maxAdventure = max(maxAdventure, grid[i][j] + nextAdv[j])

            currWays[j] = totalWays
            currAdv[j] = maxAdventure  # Remains -1 if no valid path exists

        # Move row states upwards
        nextWays = currWays
        nextAdv = currAdv

    # Results are aggregated back at the entry point (0, 0)
    finalPaths = nextWays[0]
    finalAdv = nextAdv[0] if nextAdv[0] != -1 else 0

    return [finalPaths, finalAdv]
    
grid = [[2, 3, 1, 3], 
        [3, 1, 3, 2], 
        [2, 1, 3, 1], 
        [2, 1, 1, 3]]
print(findWays(grid))
