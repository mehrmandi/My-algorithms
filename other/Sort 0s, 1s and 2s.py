def sortArray(arr):
    n = len(arr)

    zeros = []
    twos = []
    i = 0

    while i < n:
        if arr[i] == 0:
            curr = arr.pop(arr[i])
            zeros.append(curr)
            n -= 1
            print(zeros, arr)

        elif arr[i] == 2:
            curr = arr.pop(arr[i])
            twos.append(curr)
            n -= 1
            print(twos, arr)

        else:
            i += 1

    return zeros + arr + twos


arr = [0, 1, 2, 0, 1, 2]

print(sortArray(arr))