def findKthRotation(arr):
    n = len(arr)
    first = arr[0]

    arr.sort()


    for i in range(n):
        if arr[0] == first:
            return 0
        elif arr[i] == first:
            return n - i



arr = [1, 2, 3, 4, 5]
print(findKthRotation(arr))




