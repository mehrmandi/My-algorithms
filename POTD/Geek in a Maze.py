# Given a maze mat[][] of size n × m, where each cell is either:

# '.' representing an empty cell, or
# '#' representing an obstacle.
# Find the number of distinct empty cells that Geek can visit starting from the cell(r, c).

# Geek can move up, down, left, or right to an adjacent non-obstacle cell inside the maze.
# On any path, Geek can make at most u upward moves and d downward moves.
# There is no limit on the number of left or right moves.
# If the starting cell is an obstacle, return 0.
# Note:  There can be multiple paths starting from [r, c].


from collections import deque

def numberOfCells(r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
    n = len(mat)
    m = len(mat[0])

    # Starting cell is blocked.
    if mat[r][c] == '#':
        return 0

    # upUsed[i][j] = minimum number of upward moves
    # required to reach cell (i, j).
    upUsed = [
        [float('inf')] * m
        for _ in range(n)
    ]

    q = deque()

    # Starting cell.
    upUsed[r][c] = 0
    q.append((r, c))

    while q:

        x, y = q.popleft()

        # Number of upward moves used so far.
        currUp = upUsed[x][y]

        # downUsed = currUp + (x - r)
        currDown = currUp + (x - r)

        # Move Up.
        if (x - 1 >= 0 and
            mat[x - 1][y] == '.' and
            currUp + 1 <= u and
                currUp + 1 < upUsed[x - 1][y]):

            upUsed[x - 1][y] = currUp + 1

            q.append((x - 1, y))

        # Move Down.
        if (x + 1 < n and
            mat[x + 1][y] == '.' and
            currDown + 1 <= d and
                currUp < upUsed[x + 1][y]):

            upUsed[x + 1][y] = currUp

            q.append((x + 1, y))

        # Move Left.
        if (y - 1 >= 0 and
            mat[x][y - 1] == '.' and
                currUp < upUsed[x][y - 1]):

            upUsed[x][y - 1] = currUp

            q.append((x, y - 1))

        # Move Right.
        if (y + 1 < m and
            mat[x][y + 1] == '.' and
                currUp < upUsed[x][y + 1]):

            upUsed[x][y + 1] = currUp

            q.append((x, y + 1))

    # Count reachable cells.
    ans = 0

    for i in range(n):
        for j in range(m):

            if upUsed[i][j] != float('inf'):
                ans += 1

    return ans
            
            

    
r = 1
c = 0
u = 1
d = 1
mat = [['.', '.', '.'], ['.', '#', '.'], ['#', '.', '.']]
print(numberOfCells(r, c, u, d, mat))
    