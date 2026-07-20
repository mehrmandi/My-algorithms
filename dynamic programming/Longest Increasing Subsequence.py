def lIS(arr):
    n = len(arr)
    counter = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                counter[i] = max(counter[i], counter[j] + 1)

    max_num = max(counter)

    return max_num


arr = [10, 20, 35, 80]

print(lIS(arr))