def two_repeated(arr, n):

    repeated = [False for _ in range(n + 2)]
    rep = []

    for i in range(n + 2):
        if not repeated[arr[i] -1]:
            repeated[arr[i] - 1] = True
        else:
            repeated[arr[i] - 1] = False
            rep.append(arr[i])

    return rep


arr = [1, 2, 2, 1]
print(two_repeated(arr, 2))


