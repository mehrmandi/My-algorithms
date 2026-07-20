def triple_zero(arr):
    n = len(arr)
    vis = [False] * n

    i = 0
    q = []
    q.append(arr[i])
    sub_q = arr[i + 1:]


    while q:
        first = q.pop(0)

        while sub_q:
            second = sub_q.pop(0)
            double_sum = first + second

            if -double_sum in sub_q:
                return True
        i += 1
        if i < n - 2:
            q.append(arr[i])
            sub_q = arr[i + 1:]

    return False


arr = [44, 33, 18, -22, -37, -13, -35, 37, -13]
print(triple_zero(arr))
