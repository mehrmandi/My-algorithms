def subsetXORSum(arr):
    n = len(arr)
    
    #compute OR of all elements
    elem_or = 0
    
    for elem in arr:
        elem_or |= elem
        print(elem_or)
    
    # Multiply by 2^(n-1)
    return elem_or * (1 << (n - 1))


arr = [1, 2, 3]
print(subsetXORSum(arr))
