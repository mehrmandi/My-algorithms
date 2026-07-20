def sorted_array_search(arr, k):
    n = len(arr)
    low, high = 0, n
    if k == arr[low] or k == arr[high - 1]:
        return True

    while low < high - 1:
        mid_index = (low + high) // 2

        print("mid", mid_index, low, high)

        if k == arr[mid_index]:
            return True

        elif k < arr[mid_index]:
            high = mid_index

        else:
            low = mid_index

        print(high, low)

    return False

arr = [1, 3, 3, 5, 6, 6, 7, 8, 9, 9]
k = 1
print(sorted_array_search(arr, k))