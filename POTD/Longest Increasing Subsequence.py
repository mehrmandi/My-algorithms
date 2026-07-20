def lIS(arr):
    n = len(arr)
    counter = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                counter[i] = max(counter[i], counter[j] + 1)

    max_num = max(counter)

    return max_num

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(lIS(arr))
