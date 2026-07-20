from collections import deque
import sys

def nearest(grid):
    n = len(grid)
    m = len(grid[0])

    ans = [[sys.maxsize for _ in range(m)] for _ in range(n)]

    # to store the indices of the cells having 1
    q = deque()

    # visit each cell of the grid
    for i in range(n):
        for j in range(m):

            # if the cell has 1,
            # then the distance is 0
            if grid[i][j] == 1:
                ans[i][j] = 0
                q.append((i, j))

    print(q, ans)
    # iterate over all the cells
    # and find the distance of the nearest 1
    while q:
        len_q = len(q)
        print("q", q)

        for _ in range(len_q):
            x, y = q.popleft()

            # check all the four directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                # if the cell is within the grid
                # and the distance is not calculated yet
                if 0 <= x + dx < n and 0 <= y + dy < m and ans[x + dx][y + dy] == sys.maxsize:
                    ans[x + dx][y + dy] = ans[x][y] + 1
                    q.append((x + dx, y + dy))
        print("ans", ans)
    return ans


grid = [[0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1]]

print(nearest(grid))