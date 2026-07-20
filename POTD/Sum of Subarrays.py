# [Expected Approach] Element Contribution Method - O(n) Time and O(1) Space


def sumSubarray(arr):
    sum = 0

    mf = 1
   
    for i in range(len(arr) - 1, -1, -1):
        sum = sum + arr[i] * (i + 1) * mf
        
        mf += 1

    return sum


arr = [1,2, 3, 4, 5, 6, 8, 9]
print(sumSubarray(arr))

