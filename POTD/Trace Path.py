# Given a rectangular grid with n rows and m columns, and a string s representing a sequence of movement commands. Geek can start from any cell of the grid and follows all the commands in s in the same order.

# The string s consists only of the characters L, R, D, and U, where:

# L: Move one cell left, from (i, j) to(i, j - 1).
# R: Move one cell right, from (i, j) to(i, j + 1).
# D: Move one cell up, from (i, j) to(i - 1, j).
# U: Move one cell down, from (i, j) to(i + 1, j).
# Determine whether there exists at least one starting cell such that Geek remains within the grid while following all the commands in s.


# Bounding Box of Movement - O( | s|) Time and O(1) Space

def isPossible(n: int, m: int, s: str) -> bool:
    if n == 0 or m == 0:
        return False
    
    min_r, max_r = 0, 0
    min_c, max_c = 0, 0
    
    pointer_r, pointer_c = 0, 0
    
    for move in s:
        if move == "L":
            pointer_c -= 1
            min_c = min(min_c, pointer_c)
            
        elif move == "R":
            pointer_c += 1
            max_c = max(max_c, pointer_c)
            
        elif move == "U":
            pointer_r += 1
            max_r = max(max_r, pointer_r)
            
        else:
            pointer_r -= 1
            min_r = min(min_r, pointer_r)
    
    return n > (max_r - min_r) and m > (max_c - min_c)
        


n = 2
m = 3
s = "LLRU"
print(isPossible(n, m, s))
