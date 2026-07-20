# Time Complexity: O(n + k), where n is the number of trains and k is the maximum value present in the arrays.-------------------------
# Auxiliary space: O(k), where k is the maximum value present in both the arrays.-------------------------------------------


def overlapInt(arr):
    n = len(arr)
    starts = []
    ends = []
    res = 0
    
    for interval in arr:
        starts.append(interval[0])
        ends.append(interval[1])
        
    max_num = max(ends)
    
    v = [0] * (max_num + 2)
    
    for i in range(n):
        v[starts[i]] += 1
        v[ends[i] + 1] -= 1
        
    count = 0
    
    for i in range(max_num + 2):
        count += v[i]
        res = max(res, count)
        
    return res
    
    
arr = [[1, 2], [2, 4], [3, 6]]
print(overlapInt(arr))
