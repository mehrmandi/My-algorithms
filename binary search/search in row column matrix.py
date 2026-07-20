def search_matrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        if binary_search(mat[i], m, x):
            return True

    return False


def binary_search(arr, m, x):
    low = 0
    high = m - 1

    if arr[low] <= x <= arr[high]:
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == x:
                return True

            elif arr[low] <= x < arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

        return False

    return False


mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
x = 3


print(search_matrix(mat, x))