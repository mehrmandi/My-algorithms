# Given an n × 3 matrix mat[][], where each row represents the costs of three available choices at a shop, select exactly one choice from each row such that the same choice is not selected in two adjacent rows.

# Return the minimum total cost required.

# Space Optimized Approach - O(n) Time and O(1) Space

def minCost(mat):
    n = len(mat)

    # Minimum cost when the first row
    # selects each of the three choices.
    prev0 = mat[0][0]
    prev1 = mat[0][1]
    prev2 = mat[0][2]

    # Process remaining rows.
    for i in range(1, n):

        # Current row selects choice 0.
        curr0 = mat[i][0] + min(prev1, prev2)

        # Current row selects choice 1.
        curr1 = mat[i][1] + min(prev0, prev2)

        # Current row selects choice 2.
        curr2 = mat[i][2] + min(prev0, prev1)

        # Move current row values to previous row.
        prev0 = curr0
        prev1 = curr1
        prev2 = curr2

    # The last row can end with any choice.
    return min(prev0, prev1, prev2)


mat = [[1, 4 , 1], [50, 50, 50], [1, 50, 50]]
print(minCost(mat))
