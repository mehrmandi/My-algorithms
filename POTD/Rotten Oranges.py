from collections import deque

def rottenDay(mat):
    rows, cols = len(mat), len(mat[0])
    fresh_count = 0
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                fresh_count += 1
            elif mat[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    minutes = 0
    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1:
                mat[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, time + 1))
                minutes = max(minutes, time + 1)

    return minutes if fresh_count == 0 else -1



mat = [[0, 1, 2], [0, 2, 1], [2, 1, 1]]
print(rottenDay(mat))