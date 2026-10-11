# Given an integer array arr[] where the two parts around a break point are individually sorted, merge them into a single sorted array.  The break point can be anywhere in the array, including at the beginning or end.

# Merge of Merge Sort - O(n) Time and O(n) Space
def mergeTwoParts(arr):
    n = len(arr)

    # starting index of second half
    index = 0

    # Temp Array store sorted resultant array
    temp = [0] * n

    # First Find the point where array is divided
    # into two half
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            index = i + 1
            break

    # If Given array is all-ready sorted
    if index == 0:
        return

    # Merge two sorted arrays in single sorted array
    i, j, k = 0, index, 0

    while i < index and j < n:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of arr[i to index]
    while i < index:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of arr[index to n]
    while j < n:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(n):
        arr[i] = temp[i]
        
    return arr


arr = [2, 3, 8, -1, 7, 10]
print(mergeTwoParts(arr))
