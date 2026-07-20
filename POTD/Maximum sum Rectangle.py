def max_sum_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    max_sum = float('-inf')

    # Left and right boundaries of the submatrix
    for left in range(m):
        temp = [0] * n

        for right in range(left, m):
            # Compress columns into temp row sums
            for i in range(n):
                print(left, right, i, matrix[i][right])
                temp[i] += matrix[i][right]
                print(temp)

            # Apply Kadane's algorithm on temp
            curr_sum = temp[0]
            max_curr = temp[0]
            for i in range(1, n):
                curr_sum = max(temp[i], curr_sum + temp[i])
                
                max_curr = max(max_curr, curr_sum)

            max_sum = max(max_sum, max_curr)

    return max_sum


mat = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1], [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]
print(max_sum_submatrix(mat))
