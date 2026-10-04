def findPerimeter(mat):
    n = len(mat)
    m = len(mat[0])
    res = 0
    
    dirrection = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                continue
            
            
            for dir in dirrection:
                nR = i + dir[0]
                nC = j + dir[1]
                
                if nR < 0 or nR > n - 1 or nC < 0 or nC > m - 1 or mat[nR][nC] == 0:
                    res += 1
                    
    return res

mat = [[0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 0, 0]]
print(findPerimeter(mat))
