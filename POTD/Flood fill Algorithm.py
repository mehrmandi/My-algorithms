from collections import deque

def floodFill(image, sr, sc, newColor):
    n = len(image)
    m = len(image[0])
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False for _ in range(m)] for _ in range(n)]
    choice = image[sr][sc]
    q = deque()
    q.append([sr, sc])
    visited[sr][sc] = True
    image[sr][sc] = newColor


    while q:
        sz = len(q)

        for i in range(sz):
            curr = q.popleft()
            x, y = curr

            for dir in range(4):
                newX = x + direction[dir][0]
                newY = y + direction[dir][1]

                if 0 <= newX < n and 0 <= newY < m and not visited[newX][newY] and image[newX][newY] == choice:
                    image[newX][newY] = newColor
                    q.append([newX, newY])
                    visited[newX][newY] = True

    return image


image = [[1, 1, 0]]
sr = 0
sc = 2
newColor = 1

print(floodFill(image, sr, sc, newColor))
