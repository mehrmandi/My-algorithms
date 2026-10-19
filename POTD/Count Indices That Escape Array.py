# Given an array arr[], where arr[i] represents the exact number of steps to move from index i.  An index is considered good if repeatedly following the jumps eventually takes you outside the array. Otherwise, if the jumps result in an infinite loop, the index is considered bad.

# A positive value indicates a move to the right
# A negative value indicates a move to the left.
# A 0 value means no move and considered bad.
# Return the number of good indices.

# DFS with Memoization - O(n) Time and O(n) Space

def dfs(arr, i, target):
    # If the current index is outside the array bounds, it's a good index
    if i >= len(arr) or i < 0:
        return True
    
    # If the current index has a value of 0, it's a bad index
    if arr[i] == 0:
        return False
    
    # If the current index has already been visited, return False to avoid infinite loops
    if target[i] == "V":
        return False
    
    # If the current index has already been determined to be good or bad, return the corresponding value
    if target[i] == "NT":
        return False
    
    # If the current index has already been determined to be good, return True
    if target[i] == "T":
        return True
    
    # Mark the current index as visiting
    target[i] = "V"
    
    # Recursively check the next index based on the jump value at the current index
    true_target = dfs(arr, i + arr[i], target)
    
    # Mark the current index as good or bad based on the result of the recursive call
    target[i] = "T" if true_target else "NT"
    
    # Return the result of the recursive call
    return true_target


def goodIndices(arr):
    n = len(arr)
    res = 0
    target = ["NV"] * n
    #  "NV" = unvisited, "V" = visiting, "T" = good, "NT" = bad.

    for i in range(n):
        if dfs(arr, i, target):
            res += 1
            
    return res


arr = [-1, -1, -1, 1, 1]
print(goodIndices(arr))

