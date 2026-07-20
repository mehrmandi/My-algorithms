def constructArr(arr):
    m = len(arr)
    res = []
    
    if m < 2:
        return [1, arr[0] - 1]
    
    
    n  = int((1 + ((1 + 4 * (m * 2)) ** (1/2))) // 2)
    
    first_elem = (arr[0] + arr[1] - arr[n - 1]) // 2
    res.append(first_elem)
    print(res)
    
    for i in range(n - 1):
        res.append(arr[i] - res[0])
        
    return res

arr = [2, 7, 7]
print(constructArr(arr))
