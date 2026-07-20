def findMoves(chairs, passengers):
    n = len(chairs)
    chairs.sort()
    passengers.sort()
    res = 0
    
    for i in range(n):
        res += abs(chairs[i] - passengers[i])
        
    return res


chairs = [3, 1, 5]
passengers = [2, 7, 4]
print(findMoves(chairs, passengers))
