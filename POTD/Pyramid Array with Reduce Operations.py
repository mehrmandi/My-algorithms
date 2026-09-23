# Given an array arr[] consisting of stones, where arr[i] represents the height of the i-th stone.

# You need to transform the stones into a pyramid by only reducing the heights of the stones. Reducing the height of a stone by 1 costs 1 unit, and stones cannot be increased or moved.
# A valid pyramid consists of a contiguous subarray whose heights follow the pattern: 1, 2, 3, ..., x - 1, x, x - 1, ..., 2, 1 for some positive integer x.
# Every stone outside this subarray must have a height of 0.

# Find the minimum total cost required to build a pyramid. It is guaranteed that at least one valid pyramid can always be formed.

# Using Left and Right DP - O(n) Time and O(n) Space

def formPyramid(arr):
    n = len(arr)
    totalHeight = 0

    # Calculate the total height of all stones.
    for i in range(n):
        totalHeight += arr[i]

    # For arrays of size 1 or 2, the only possible pyramid
    # has height 1, so the remaining stones must be reduced to 0.
    if n <= 2:
        return totalHeight - 1

    left = [0] * n
    right = [0] * n

    # left[i] = Maximum possible pyramid height at index i
    # considering only the left side.
    left[0] = 1
    for i in range(1, n):
        left[i] = min(left[i - 1] + 1, arr[i])

    # right[i] = Maximum possible pyramid height at index i
    # considering only the right side.
    right[n - 1] = 1
    for i in range(n - 2, -1, -1):
        right[i] = min(right[i + 1] + 1, arr[i])

    minCost = float('inf')

    # Try every index as the peak of the pyramid.
    for i in range(n):

        # The peak height is limited by both the left and right constraints.
        peakHeight = min(left[i], right[i])

        # A pyramid of height h has a total sum of h².
        pyramidSum = peakHeight * peakHeight

        # Cost = Original total height - Height of the constructed pyramid.
        minCost = min(minCost, totalHeight - pyramidSum)

    return minCost


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 1]
    print(formPyramid(arr))
