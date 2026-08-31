# Given four integers n, i, d, and c, where:

# i is the cost of inserting a single character,
# d is the cost of deleting the last character,
# c is the cost of copying the entire current string and pasting it immediately(thereby doubling its length).
# Find the minimum cost required to obtain exactly n characters on the screen. Initially, the screen is empty.

# Using Dynamic Programming with Tabulation - O(n) Time and O(n) Space


def minCost(n: int, i: int, d: int, c: int) -> int:
    # dp[x] represents the minimum cost required to obtain exactly x characters.
    dp = [0 for _ in range(n + 1)]
    
    # One insertion is required to obtain the first character.
    dp[1] = i
    
 
    for j in range(2, n + 1):
        # Option 1: Insert one character after reaching j - 1 characters.
        new_add = dp[j - 1] + i
        
        # If j is odd, we need to copy from j//2 + 1 characters # and then delete one extra character. 
        # For even j, no deletion is needed.
        delete_extra = 0 if j % 2 == 0 else 1
        
        # Option 2: # Reach j//2 (or j//2 + 1 for odd j), 
        # copy the entire string, and delete one character if necessary.
        new_minus = dp[j // 2 + delete_extra] + c + delete_extra * d
        
        # Choose the cheaper of the two possible operations.
        dp[j] = min(new_add, new_minus)
    
    # Return the minimum cost required to obtain exactly n characters.        
    return dp[n]


n = 9
i = 10
d = 1
c = 1

print(minCost(n, i, d, c))
