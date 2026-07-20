def subarrayXor(arr):
    n = len(arr)
    res = 0
   
    for i in range(n):
        if ((n - i)*(i - 1)) % 2 == 1:
            res = res ^ arr[i]
        
    return res
        
    
arr = [3, 9, 1, 2, 6]
print(subarrayXor(arr))