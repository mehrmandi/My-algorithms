# Given a 2D binary matrix mat[][] consisting only of 0s and 1s, find the area of the largest rectangle sub-matrix that contains only 1s.

# Using Largest Rectangular Area in a Histogram - O(n * m) Time and O(m) Space


from typing import List

# Function to find the maximum area of
# rectangle in a histogram.


def getMaxArea(arr: List[int]) -> int:
    n = len(arr)
    s = []
    res = 0
    tp, curr = 0, 0
    for i in range(n):
        while s and arr[s[-1]] >= arr[i]:
            # The popped item is to be considered as the
            # smallest element of the histogram
            tp = s.pop()

            # For the popped item previous smaller element is
            # just below it in the stack (or current stack top)
            # and next smaller element is i
            width = i if not s else i - s[-1] - 1

            res = max(res, arr[tp] * width)
        s.append(i)

    # For the remaining items in the stack, next smaller does
    # not exist. Previous smaller is the item just below in
    # stack.
    while s:
        tp = s.pop()
        curr = arr[tp] * (n if not s else n - s[-1] - 1)
        res = max(res, curr)

    return res

# Function to find the maximum area of rectangle
# in a 2D matrix.


def maxArea(mat: List[List[int]]) -> int:
    n = len(mat)
    m = len(mat[0])

    # Array to store matrix
    # as a histogram.
    arr = [0] * m

    res = 0

    # Traverse row by row.
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                arr[j] += 1
            else:
                arr[j] = 0

        res = max(res, getMaxArea(arr))

    return res


if __name__ == "__main__":
    mat = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]

    print(maxArea(mat))

