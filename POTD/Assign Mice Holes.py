def assignHole(mices, holes):
    mices.sort()
    holes.sort()
    
    n = len(mices)
    res = 0
    
    for i in range(n):
        res = max(res, abs(mices[i] - holes[i]))
        
    return res


mices = [1, 2]
holes = [20, 10]
print(assignHole(mices, holes))

