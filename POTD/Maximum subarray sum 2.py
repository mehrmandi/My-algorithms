from collections import deque


def maxSubarrSum(arr, a, b):

    n = len(arr)

    # compute prefix sum of the array
    for i in range(1, n):
        arr[i] += arr[i - 1]

    # to store the maximum sum found
    maxi = arr[a - 1]

    # deque to maintain the minimum prefix in
    # the current window
    dq = deque()

    # insert initial prefix 0
    dq.append(0)

    # iterate from index 'a' to 'n - 1' (inclusive)
    for i in range(a, n):

        # remove prefix[i - b - 1] from deque if it's
        # outside the valid window
        if i - b - 1 >= 0:
            if dq[0] == arr[i - b - 1]:
                dq.popleft()
        # special case: remove 0 if it falls outside the window
        elif i - b == 0:
            if dq[0] == 0:
                dq.popleft()

        # maintain increasing order in deque (monotonic queue)
        while dq and dq[-1] > arr[i - a]:
            dq.pop()

        # insert current prefix sum for future subarray starts
        dq.append(arr[i - a])

        # compute maximum subarray sum ending at index i
        maxi = max(maxi, arr[i] - dq[0])

    return maxi


if __name__ == "__main__":
    arr = [4, 5, -1, -2, 6]
    a = 2
    b = 4
    res = maxSubarrSum(arr, a, b)
    print(res)
    
