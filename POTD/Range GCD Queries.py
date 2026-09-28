# Given an array arr[] and a series of queries q[][]. Each query can be one of the following two types:

# Update query: 1 index value — Update the element at position index to value.
# GCD query: 2 L R — Find the GCD of all elements in the range[L, R](both inclusive).
# We need to process all the queries in order and return a vector of integers containing the results of all GCD queries.

# Segment Tree for Range GCD - O((n + q) log(n)) Time and O(n) Space

import math
from typing import List

# Function to compute GCD of two numbers


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

# Get mid index


def getMid(s: int, e: int) -> int:
    return s + (e - s) // 2

# Build segment tree


def buildSegmentTree(arr: List[int], ss: int, se: int, st: List[int], si: int) -> int:
    if ss == se:
        st[si] = arr[ss]
        return arr[ss]
    mid = getMid(ss, se)
    st[si] = gcd(
        buildSegmentTree(arr, ss, mid, st, si * 2 + 1),
        buildSegmentTree(arr, mid + 1, se, st, si * 2 + 2)
    )
    return st[si]

# Query GCD in range


def findGcd(ss: int, se: int, qs: int, qe: int, si: int, st: List[int]) -> int:
    if ss > qe or se < qs:
        return 0
    if qs <= ss and qe >= se:
        return st[si]
    mid = getMid(ss, se)
    return gcd(
        findGcd(ss, mid, qs, qe, 2 * si + 1, st),
        findGcd(mid + 1, se, qs, qe, 2 * si + 2, st)
    )

# Update value in segment tree


def updateValueUtil(ss: int, se: int, index: int, new_val: int, si: int, st: List[int]):
    if index < ss or index > se:
        return
    if ss == se:
        st[si] = new_val
        return
    mid = getMid(ss, se)
    if index <= mid:
        updateValueUtil(ss, mid, index, new_val, 2 * si + 1, st)
    else:
        updateValueUtil(mid + 1, se, index, new_val, 2 * si + 2, st)
    st[si] = gcd(st[2 * si + 1], st[2 * si + 2])


def updateValue(index: int, new_val: int, arr: List[int], st: List[int], n: int):
    arr[index] = new_val
    updateValueUtil(0, n - 1, index, new_val, 0, st)


def processQueries(arr: List[int], q: List[List[int]]) -> List[int]:
    n = len(arr)
    x = 2 * int(2 ** math.ceil(math.log2(n))) - 1
    st = [0] * x
    buildSegmentTree(arr, 0, n - 1, st, 0)

    result = []
    for query in q:
        type_ = query[0]
        if type_ == 1:
            index = query[1]
            new_val = query[2]
            updateValue(index, new_val, arr, st, n)
        else:
            l, r = query[1], query[2]
            result.append(findGcd(0, n - 1, l, r, 0, st))
    return result


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 6, 8, 16]
    q = [
        [2, 0, 2],
        [1, 3, 8],
        [2, 2, 5]
    ]
    ans = processQueries(arr, q)
    print(*ans)

arr = [2, 3, 4, 6, 8, 16]
q = 3
queries = [[0, 0, 2], [1, 3, 8], [0, 2, 5]]
print(processQueries(arr, queries))
