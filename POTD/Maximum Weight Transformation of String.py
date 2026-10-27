# Given a string s consisting only of the characters 'A' and 'B', you can toggle any character. A toggle changes 'A' to 'B' or 'B' to 'A'.

# The weight of a string is calculated using the following rules:

# An alternating adjacent pair("AB" or "BA") contributes 4 to the weight.
# Each character can belong to at most one pair, so the pairs must not overlap.
# Every character that does not belong to any pair contributes 1 to the weight.
# Each toggle performed decreases the total weight by 1.
# Therefore, Weight = Weight of alternating adjacent pairs + Weight of characters that do not belong to any pair - Number of Toggles

# You can toggle characters to make adjacent characters different and form pairs. Find the maximum possible weight obtainable from the string by choosing pairs and toggling characters optimally.

# Space-Optimized DP - O(n) Time and O(1) Space

def getMaxWeight(s):
    n = len(s)
    
    if n == 0:
        return 0
    
    prev = 0
    curr = 1
    
    for i in range(1, n):
        add = 4 if s[i] != s[i - 1] else 3
        new = max(curr + 1, prev + add)
        prev = curr
        curr = new
       
    return curr


s = "AA"

print(getMaxWeight(s))
