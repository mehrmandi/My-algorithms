# Given an array arr[] of size n, partition its elements into a strictly increasing subsequence and a strictly decreasing subsequence.

# Each element can belong to at most one of these subsequences, and some elements may remain unused.

# Determine the minimum number of elements that cannot be included in either subsequence.

# Space Optimized Approach - O(n ^ 3) Time and O(n ^ 2) Space


def minCount(arr):

    n = len(arr)

    # Stores DP values for idx + 1.
    next = [[0] * (n + 1) for _ in range(n + 1)]

    # Stores DP values for the current index.
    curr = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the DP table in reverse order.
    for idx in range(n - 1, -1, -1):

        for incLast in range(-1, n):

            for decLast in range(-1, n):

                # Option 1: Skip the current element.
                ans = 1 + next[incLast + 1][decLast + 1]

                # Option 2: Include in increasing subsequence.
                if incLast == -1 or arr[idx] > arr[incLast]:
                    ans = min(ans,
                              next[idx + 1][decLast + 1])

                # Option 3: Include in decreasing subsequence.
                if decLast == -1 or arr[idx] < arr[decLast]:
                    ans = min(ans,
                              next[incLast + 1][idx + 1])

                curr[incLast + 1][decLast + 1] = ans

        # Move the current layer to the next layer.
        next, curr = curr, next

    return next[0][0]


arr = [3, 1, 2, 5, 4]
print(minCount(arr))
    
