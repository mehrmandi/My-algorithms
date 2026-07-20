def findUnion(a, b):
    union_arr = list(set(a + b))
    
    return union_arr

a = []
b = [4, 5, 6, 3, 1]
print(findUnion(a, b))
