def value_index(arr):
    i = 1
    equal = []

    while i <= len(arr):
        if arr[i - 1] == i:
            equal.append(i)

        i += 1

    return equal


arr = [15, 2, 45, 4 , 7]
print(value_index(arr))