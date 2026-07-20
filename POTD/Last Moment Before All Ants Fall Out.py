def getLastMoment(n, left, right):
    if not left and not right:
        return -1
    
    for i in range(len(left)):
        right.append(n - left[i])
        
    return n - min(right)

n = 9
left = []
right = []
print(getLastMoment(n, left, right))
