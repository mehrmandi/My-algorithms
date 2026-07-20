# function to count the number of elements
# less than or equal to x
def countSmallerEqual(mat, x):
    n = len(mat)
    count = 0
    row = 0
    col = n - 1

    # traverse from the top-right corner
    while row < n and col >= 0:
        if mat[row][col] <= x:

            # if current element is less than
            # or equal to x, all elements in this
            # row up to the current column are <= x
            count += (col + 1)
            row += 1
        else:
            # move left in the mat
            col -= 1

    return count

# function to find the kth smallest
# element in a sorted 2D mat


def kthSmallest(mat, k):
    n = len(mat)
    low = mat[0][0]
    high = mat[n - 1][n - 1]
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2

        # count elements less than or equal to mid
        count = countSmallerEqual(mat, mid)

        if count < k:

            # if there are less than k elements
            # <= mid, the kth smallest is larger
            low = mid + 1
        else:

            # otherwise, mid might be the answer,
            # but we need to check for smaller values
            ans = mid
            high = mid - 1

    return ans


if __name__ == "__main__":
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]
    k = 3
    result = kthSmallest(mat, k)
    print(result)
