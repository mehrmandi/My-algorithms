# Given a string s made of two characters of 'x' and 'y'.  The task is to verify whether s is made by concatenating substrings that follow the pattern xnyn(equal number of y's follow equal number of x's).

# Single Traversal - O(n) Time and O(1) Space

def findPattern(s):
    n = len(s)
    res = 0
    i = 0

    while res == 0 and i < n:
        while  i < n and s[i] == "x":
            res += 1
            i += 1
            
        while i < n and s[i] == "y":
            res -= 1
            i += 1
      
    return res == 0 and i == n
    

s = "xxxyyy"
print(findPattern(s))
