# Given a string s consisting of lowercase English letters and an integer array roll[], perform a sequence of roll operations on the string.

# For each value roll[i], increment each of the first roll[i] characters of the string by 1 in the English alphabet. After 'z', the character wraps around to 'a'.

# Return the final string after applying all roll operations.

# Note: A roll operation affects the current state of the string, including all previous modifications.

# Difference Array and Prefix Sum - O(n + m) Time and O(n) Space

def findRollOut(s, roll):
    n = len(s)
    arr = [0] * n
    s = list(s)
    
    
    for j in roll:
        arr[j - 1] += 1
        
    count = 0
    
    for i in range(n - 1, -1, -1):
        count += arr[i]
        arr[i] = count
        
        s[i] = chr((ord(s[i]) - ord('a') + count) % 26 + ord('a'))
    
      
    return ''.join(s)


s = "zcza"
roll = [1, 1, 3, 4]
print(findRollOut(s, roll))
