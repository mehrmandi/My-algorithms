# Given a 2D grid mat[][] of size n × m consisting of characters and a string word, find all starting positions where the word occurs in the grid.

# The word can be formed from any cell by moving in any of the 8 directions(2 horizontal, 2 vertical, and 4 diagonal) in a straight line without changing direction.
# Each cell can be used at most once per occurrence.
# Return all unique starting coordinates in lexicographically smallest order.

# Iterative - O(m × n × WordLength) Time and O(1) Space


# This function searches for the given word
# in all 8 directions from the coordinate.
def wordCheck(mat, r, c, word, n, m, lenWord):
    if mat[r][c] != word[0]:
        return False
    
    directions = [[0, 1], [0, -1], [1, 0], [1, -1], [1, 1], [-1, 0], [-1, 1], [-1, -1]]
    
    for dir in directions:
        nr , nc = r + dir[0], c + dir[1]
        k = 1
        
        while k < lenWord:
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                break
            
            if mat[nr][nc] != word[k]:
                break
            
            nr += dir[0]
            nc += dir[1]
            k += 1
            
        if k == lenWord:
            return True
    
    return False
    

def searchWord(mat, word):
    n = len(mat)
    m = len(mat[0])
    lenWord = len(word)
    res = []
    
    # if the word is found from this coordinate,
    # then append it to result.
    
    for i in range(n):
        for j in range(m):
            if wordCheck(mat, i, j, word, n, m, lenWord):
                res.append([i, j])
    
    
    return res
    
    
grid = [['a', 'b', 'a', 'b'],
        ['a', 'b', 'e', 'b'],
        ['e', 'b', 'e', 'b']]
word = "abe"
print(searchWord(grid, word))