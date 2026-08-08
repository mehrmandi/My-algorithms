# Given a square matrix mat[][] of size n * n. A zigzag sequence starts from the top and ends at the bottom. 
# Two consecutive elements of sequence cannot belong to the same column. Return the maximum sum of such a zigzag sequence.

# Using Space-Optimized Dynamic Programming- O(n ^ 2) Time and O(n) Space


def zigzagSequence(mat):
    n = len(mat)

    # DP values for the previous row
    prev = mat[0]

    for i in range(1, n):
        max1 = -1
        max2 = -1
        maxCol = -1

        # Find the maximum and second maximum
        # values from the previous row
        for j in range(n):
            if prev[j] > max1:
                max2 = max1
                max1 = prev[j]
                maxCol = j
            elif prev[j] > max2:
                max2 = prev[j]

        curr = [0] * n
        
        print(max1, max2, maxCol)

        for j in range(n):

            # Use second maximum if the current column
            # is the same as the column of the maximum value
            curr[j] = mat[i][j] + (max2 if j == maxCol else max1)

        # Move to the next row.
        print(curr)
        prev = curr

    # Find the maximum zigzag sum
    res = max(prev)

    return res


    
mat = [[1, 2, 4, 12], 
       [3, 9, 6, 8], 
       [11, 3, 15, 25], 
       [7, 6, 9, 1]]
print(zigzagSequence(mat))
