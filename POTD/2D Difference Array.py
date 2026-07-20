def apply_operations(mat, operations):
    rows, cols = len(mat), len(mat[0])

    # Step 1: Create a difference matrix initialized to 0
    diff = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Step 2: Apply each operation to the difference matrix
    for v, r1, c1, r2, c2 in operations:
        print(v, r1, c1, r2, c2, diff)
        diff[r1][c1] += v
        diff[r1][c2 + 1] -= v
        diff[r2 + 1][c1] -= v
        diff[r2 + 1][c2 + 1] += v
        
    print("diff", diff)

    # Step 3: Convert difference matrix to actual updates using prefix sums
    for r in range(rows):
        for c in range(cols):
            if r > 0:
                diff[r][c] += diff[r - 1][c]
            if c > 0:
                diff[r][c] += diff[r][c - 1]
            if r > 0 and c > 0:
                diff[r][c] -= diff[r - 1][c - 1]

    # Step 4: Add the diff matrix to the original matrix
    for r in range(rows):
        for c in range(cols):
            mat[r][c] += diff[r][c]

    return mat


mat = [[1, 2, 3],
       [1, 1, 0],
       [4, -2, 2]]


opr = [[2, 0, 0, 1, 1], [-1, 1, 0, 2, 2]]

print(apply_operations(mat, opr))
