dir = "DLRU"
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def isValid(nX, nY, n, maze):
    return nX >= 0 and nY >= 0 and nX < n and nY < n and maze[nX][nY] == 1


def possibleRoutRec(maze, X, Y, path, res, n):
    if X == n - 1 and Y == n - 1:
        res.append("".join(path))
        return
    
    maze[X][Y] = 0
    
    for i in range(4):
        
        nX, nY = X + dx[i], Y + dy[i]
        if isValid(nX, nY, n, maze):
            path.append(dir[i])
            possibleRoutRec(maze, nX, nY, path, res, n)
            
            path.pop()
   
    maze[X][Y] = 1

def ratInMaze(maze):
    n  = len(maze)
    
    res = []
    path = []
    
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return res
    
    possibleRoutRec(maze, 0, 0, path, res, n)
    
    res.sort()
    
    return res




maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]


print(ratInMaze(maze))


