# [Expected Approach] Using Sorting - O(n*log(n)) Time and O(1) Space------------

def canAttend(arr):
    n = len(arr)
    arr.sort()

    for i in range(1, n):
        if arr[i][0] < arr[i - 1][1]:
            return False
    
    return True
            
        
arr = [[2, 4], [9, 12], [6, 10]]
print(canAttend(arr))
