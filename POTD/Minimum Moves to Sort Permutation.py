def minMoves(arr):
    n = len(arr)
    
    pos_hash = {num: i for i, num in enumerate(arr)}
    
    LCSI = 0
    current_chain = 0
    
    for i in range(1, n + 1):
        if i == 1 or pos_hash[i] > pos_hash[i - 1]:
            current_chain += 1
        
        else:
            current_chain = 1
    
        LCSI = max(LCSI, current_chain)
    
    
    return n - LCSI
         
            
arr = [6, 2, 4, 3, 1, 5]
print(minMoves(arr))
