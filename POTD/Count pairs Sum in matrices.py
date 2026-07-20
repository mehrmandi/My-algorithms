# O(n^3 * log(n)) time complexity----------------------------------------------------

def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    lo, hi = 0, n * m - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        # Find row and column of element at mid index
        row = mid // m
        col = mid % m

        # If x is found, return true
        if mat[row][col] == x:
            return True

        # If x is greater than mat[row][col], search in
        # right half
        if mat[row][col] < x:
            lo = mid + 1

        # If x is less than mat[row][col], search in
        # left half
        else:
            hi = mid - 1

    return False

def countPairSum(mat1, mat2, x):
    n = len(mat1)
    count = 0
    
    for i in range(n):
        for j in range(n):
            pair_num = x - mat1[i][j]
            if searchMatrix(mat2, pair_num):
                count += 1
                
    return count



n = 2 
x = 10
mat1 = [[1, 2], [3, 4]]
mat2 = [[4, 5], [6, 7]]
print(countPairSum(mat1, mat2, x))


# Python program to Count pairs from
# two sorted matrices with given sum
# [Expected Approach] Using Two Pointers - O(n2) Time and O(1) Space-----------------------------------------
# Function to count pairs from two sorted matrices
# whose sum is equal to a given value x
# def countPairs(mat1, mat2, x):
#     n = len(mat1)

#     # Indices for pointing current element in mat1 and mat2
#     i, j = 0, (n*n - 1)

#     count = 0

#     # While there are elements in both matrices
#     while i < n*n and j >= 0:
#         r1, c1 = i//n, i % n
#         r2, c2 = j//n, j % n
#         val = mat1[r1][c1] + mat2[r2][c2]

#         if val == x:
#             count += 1

#             # Move i and j
#             i += 1
#             j -= 1
#         elif val < x:
#             i += 1
#         else:
#             j -= 1

#     return count


# if __name__ == "__main__":
#     mat1 = [
#         [1, 5, 6],
#         [8, 10, 11],
#         [15, 16, 18]
#     ]

#     mat2 = [
#         [2, 4, 7],
#         [9, 10, 12],
#         [13, 16, 20]
#     ]

#     x = 21

#     print(countPairs(mat1, mat2, x))


# Python program to Count pairs from
# two sorted matrices with given sum
# [Better Approach] Using Hash Set - O(n^2) Time and O(n^2) Space--------------------------------------
# Function to count pairs from two sorted matrices
# whose sum is equal to a given value x
# def countPairs(mat1, mat2, x):

#     # Insert all elements of mat2 into the set
#     elements = set()
#     for row in mat2:
#         for elem in row:
#             elements.add(elem)

#     # For each element of mat1, check if
#     # (x - element) is in the set
#     count = 0
#     for row in mat1:
#         for elem in row:
#             if (x - elem) in elements:
#                 count += 1
#     return count


# if __name__ == "__main__":
#     mat1 = [
#         [1, 5, 6],
#         [8, 10, 11],
#         [15, 16, 18]
#     ]

#     mat2 = [
#         [2, 4, 7],
#         [9, 10, 12],
#         [13, 16, 20]
#     ]

#     x = 21

#     print(countPairs(mat1, mat2, x))
