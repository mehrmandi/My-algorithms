def uniqueNumber(arr):
    arr.sort()
    n = len(arr)
    res = []
    count = 0
    i = 0

    while i < n:
        if count == 2:
            return res

        if i < n - 1:
            if arr[i] == arr[i + 1]:
                i += 2

            elif arr[i] != arr[i + 1]:
                res.append(arr[i])
                i += 1
                count += 1

        elif i == n - 1:
            res.append(arr[i])
            i += 1
            count += 1

    return res


arr = [2, 1, 3, 2]
print(uniqueNumber(arr))
