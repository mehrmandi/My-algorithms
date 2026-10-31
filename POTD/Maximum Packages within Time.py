# A delivery agent has to deliver packages at locations arranged in a line. The number of packages at the ith location is given by arr[i].

# The agent can start at any location and can only visit consecutive locations.
# Time required for every location is 1 unit.
# Given arr[] and totalTime, find the maximum number of packages the agent can deliver within totalTime.


# Sliding Window - O(n) Time and O(1) Space

def maxPackages(arr: list[int], totalTime: int) -> int:
    n = len(arr)
    
    if n <= totalTime:
        return sum(arr)
    
    l = 0
    win_sum = sum(arr[:l + totalTime])
    res = win_sum
    
    while l + totalTime < n:
        win_sum += (arr[l + totalTime] - arr[l])
        res = max(res, win_sum)
        l += 1
        
    return res
    
    
arr = [1, 6, 2, 5, 3, 4]
totalTime = 2
print(maxPackages(arr, totalTime))
        
        
        
    
