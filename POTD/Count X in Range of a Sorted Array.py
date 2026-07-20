import bisect

def countXInRange(arr, queries):
    res = []
    for q in queries:
        l, r, x = q[0], q[1], q[2]
        
        left_idx = bisect.bisect_left(arr, x, l, r + 1)
        right_idx = bisect.bisect_right(arr, x, l, r + 1)
        
        res.append(right_idx - left_idx)
    
    return res

arr = [1, 2, 2, 4, 5, 5, 5, 8]
queries = [[0, 7, 5], [1, 2, 2], [0, 3, 7]]
print(countXInRange(arr, queries))
