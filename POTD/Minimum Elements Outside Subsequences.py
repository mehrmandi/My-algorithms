# Given an array arr[] of size n, partition its elements into a strictly increasing subsequence and a strictly decreasing subsequence.

# Each element can belong to at most one of these subsequences, and some elements may remain unused.

# Determine the minimum number of elements that cannot be included in either subsequence.

# Space Optimized Approach - O(n ^ 3) Time and O(n ^ 2) Space


def minCount(arr):

    n = len(arr)

    dp = [[[0] * (n + 1) for _ in range(n + 1)]
          for _ in range(n + 1)]

    for idx in range(n - 1, -1, -1):

        for incLast in range(-1, n):

            for decLast in range(-1, n):

                ans = 1 + dp[idx + 1][incLast + 1][decLast + 1]

                if incLast == -1 or arr[idx] > arr[incLast]:
                    ans = min(ans,
                              dp[idx + 1][idx + 1][decLast + 1])

                if decLast == -1 or arr[idx] < arr[decLast]:
                    ans = min(ans,
                              dp[idx + 1][incLast + 1][idx + 1])

                dp[idx][incLast + 1][decLast + 1] = ans

    return dp[0][0][0]


arr = [3, 1, 2, 5, 4]
print(minCount(arr))
    
