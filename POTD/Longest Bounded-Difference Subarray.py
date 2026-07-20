from collections import deque

def longestBoundedSub(arr, k):
    minq, maxq = deque(), deque()
    st, end = 0, 0
    ansLen = 0
    ansSt, ansEnd = 0, 0
    for i in range(len(arr)):
        end = i
        while maxq and arr[maxq[-1]] < arr[i]:
            maxq.pop()
        maxq.append(i)

        while minq and arr[minq[-1]] > arr[i]:
            minq.pop()
        minq.append(i)

        while arr[maxq[0]] - arr[minq[0]] > x:
            st += 1
            while minq and minq[0] < st:
                minq.popleft()
            while maxq and maxq[0] < st:
                maxq.popleft()

        if end - st + 1 > ansLen:
            ansLen = end - st + 1
            ansSt, ansEnd = st, end

    return arr[ansSt:ansEnd + 1]





arr = [8, 4, 2, 6, 7]
x = 4
print(longestBoundedSub(arr, x))


