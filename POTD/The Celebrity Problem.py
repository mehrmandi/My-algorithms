# def celebrity(mat):
#     n = len(mat)
#     pot_row = []
#     hash = {}
    
    
    
#     for row in range(n):
#         if sum(mat[row]) == 1:
#             pot_row.append(row)
            
            
#     for row in mat:
#         for col in pot_row:
#             if row[col] == 1:
#                 hash[col] = hash.get(col, 0) + 1
#             if col in hash and hash[col] == n:
#                 return col
            
#     return -1
    

# mat = [[1, 0],
#        [0, 1]]
# print(celebrity(mat))

# [Expected Approach] Using Two Pointers - O(n) Time and O(1) Space--------------------------------


def celebrity(mat):
    n = len(mat)

    i = 0
    j = n - 1
    while i < j:

        # j knows i, thus j can't be celebrity
        if mat[j][i] == 1:
            j -= 1

        # else i can't be celebrity
        else:
            i += 1

    # i points to our celebrity candidate
    c = i

    # check if c is actually
    # a celebrity or not
    for i in range(n):
        if i == c:
            continue

        # if any person doesn't
        # know 'c' or 'c' doesn't
        # know any person, return -1
        if mat[c][i] or not mat[i][c]:
            return -1

    return c


if __name__ == "__main__":
    mat = [[1, 1, 0],
           [0, 1, 0],
           [0, 1, 1]]
    print(celebrity(mat))
