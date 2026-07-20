def subarrayXor(arr, k):
    XOR_hash = {}
    prefX = 0
    count = 0
    
    for elem in arr:
        prefX ^= elem
        
        if prefX == k:
            count += 1
                 
        count += XOR_hash.get(prefX ^ k, 0)
        
        
        XOR_hash[prefX] = XOR_hash.get(prefX, 0) + 1
    
    return count
        
    
        
        
arr = [4, 2, 2, 6, 4]
k = 6

print(subarrayXor(arr, k))
