def sortAfterEquation(arr, A, B, C):
    new_arr = []
    for i in arr:
        eq = A * (i ** 2) + B * i + C
        new_arr.append(eq)
    new_arr.sort()
    return new_arr


arr = [-3, -1, 2, 4]
A = -1
B = 0
C = 0
print(sortAfterEquation(arr, A, B, C))
        
    