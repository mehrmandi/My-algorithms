# Given a string s and an integer pos, an infinite string is constructed by repeatedly applying the following operation. In the i-th step, append i consecutive $ characters, followed by the reverse of the current string, to the current string.

# Formally, if the current string is s, update it as:

# s = s + ('$' repeated i times) + reverse(s)
# The initial string is the given s, and the process continues indefinitely.

# Find and return the character at the pos(1-based indexing) in the resulting infinite string.

# Recursive Structure of Resultant String - O(log(pos)) Time and O(1) Space

def posInfinite(s: str, pos: int) -> str:
    n = len(s)
    
    new_s = n
    step = 1
    
    while new_s < pos:
        new_s = new_s * 2 + step
        step += 1
        
    while step > 1:
        prev_step = (new_s - (step - 1)) // 2
        
        if pos > prev_step and pos <= prev_step + step - 1:
            return "$"
        
        if pos <= prev_step:
            new_s = prev_step
            
        else:
            pos = new_s - pos + 1
            new_s = prev_step
            
        step -= 1
        
    return s[pos - 1]

s = "abc"
pos = 7
print(posInfinite(s, pos))
