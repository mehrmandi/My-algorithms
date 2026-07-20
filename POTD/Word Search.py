# You are given a matrix mat[][] of size n*m containing english alphabets and a string word. 
# Check if the word exists on the mat[][] or not . 
# The word can be constructed by using letters from adjacent cells, either horizontally or vertically. 
# The same cell cannot be used more than once.

def isWordExist(mat, word):
    n, m = len(mat), len(mat[0])
    
    def dfs(i, j, k):
        if k == len(word):
            return True
        
        if (i < 0 or i >= n or j < 0 or j >= m or
                mat[i][j] != word[k]):
            return False
        
        temp = mat[i][j]
        mat[i][j] = "#"
        
        found = (dfs(i + 1, j, k + 1) or 
                 dfs(i - 1, j, k + 1) or 
                 dfs(i, j + 1, k + 1) or 
                 dfs(i, j - 1, k + 1))
        
        mat[i][j] = temp
        return found
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
    
    return False   
    

mat = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word = "GEAK"
print(isWordExist(mat, word))
