from collections import deque

def maxOfSubarrays(arr, k):
    n = len(arr)

    res = []

    dq = deque()

    for i in range(0, k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    for i in range(k, len(arr)):
        res.append(arr[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    res.append(arr[dq[0]])

    return res



arr = [3, 2, 1, 1, 4, 5, 2, 3, 6]
k = 3

print(maxOfSubarrays(arr, k))



