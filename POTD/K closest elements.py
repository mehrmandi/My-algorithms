def printKClosest(arr, k, x):
    # code here
    arr = [num for num in arr if num != x]

    # Sort based on distance from x, break ties by preferring larger number
    sorted_by_closeness = sorted(arr, key=lambda num: (abs(num - x), -num))

    # Take the first k elements
    result = sorted_by_closeness[:k]

    return result

    
    
arr = [5, 63]
k = 2
x = 85
# print(array_search(arr, x))
print(printKClosest(arr, k, x))
