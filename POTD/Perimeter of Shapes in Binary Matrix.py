# Given a binary matrix mat[][] of size n × m, where each cell contains either 0 or 1, find the total perimeter of all figures formed by cells containing 1s. Two cells are considered adjacent if they share a common side.

# A single cell containing 1 has a perimeter of 4, whereas two adjacent cells containing 1 (i.e., 11) together have a perimeter of 6.

# Count the Exposed Sides of Each 1 - O(n * m) Time and O(1) Space


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
