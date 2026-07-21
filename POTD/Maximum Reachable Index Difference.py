# Using Dynamic Programming(Right-to-Left Traversal) - O(n) Time and O(1) Space

def maxIndexDifference(s):
    n = len(s)
    # Initialize an array to store the farthest reachable index for each character
    position = [-1] * 26
    
    # Initialize the result variable to store the maximum reachable index difference if not 'a' is found then return -1
    res = -1
    
    # Right-to-Left Traversal to find the maximum reachable index difference
    for i in range(n - 1, -1, -1):
        # farthest reachable index for the current character
        maxR = i
        
        # If the current character is not 'z' and there exists a character greater than the current character, update maxR to the farthest reachable index of that character     
        if s[i] != 'z' and position[ord(s[i]) - ord('a') + 1] != -1:
            maxR = position[ord(s[i])- ord('a') + 1]
            
        # update the position of the current character to the maximum reachable index   
        position[ord(s[i]) - ord('a')] = max(position[ord(s[i]) - ord('a')], maxR)
        
        # If the current character is 'a', calculate the difference between the farthest reachable index and the current index, and update the result if it's greater than the previous maximum difference
        if s[i] == 'a':
            res = max(res, maxR - i)
            
    return res
        


s = "abcbzzd"
print(maxIndexDifference(s))
