def findInterval(prefix, low, high, rank):

    while low < high:

        mid = low + (high - low) // 2

        if prefix[mid] < rank:
            low = mid + 1
        else:
            high = mid

    return low


def getMarks(l, r, rank):

    n = len(l)

    # Stores the cumulative number of marks till each interval
    prefix = [0] * n

    prefix[0] = r[0] - l[0] + 1

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + (r[i] - l[i] + 1)

    ans = [0] * len(rank)

    # Process every query
    for i in range(len(rank)):

        # Find the interval containing the required rank
        idx = findInterval(prefix, 0, n - 1, rank[i])

        # Compute the corresponding mark
        diff = prefix[idx] - rank[i]
        ans[i] = r[idx] - diff

    return ans


l = [1, 6, 14]
r = [3, 9, 15]
rank = [2, 5, 8]

print(getMarks(l, r, rank))
