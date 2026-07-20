# from copy import deepcopy


# # Time O(n^2 * m log m)----------------------------------
# def findRectangle(mat):
#     n, m = len(mat), len(mat[0])
#     if n <= 1 or m <= 1:
#         return False
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             index = deepcopy(mat[i])
#             for k in range(m):
#                 if mat[j][k] == 1:
#                     index[k] += 1
#             index.sort(reverse=True)
#             if index[0] >= 2 and index[1] >= 2:
#                 return True
            
#     return False


# mat = [[1, 0, 1, 1, 0],
#        [0, 0, 1, 0, 1],
#        [0, 0, 0, 1, 0],
#        [1, 0, 1, 0, 0]]

# print(findRectangle(mat))


# [Better Approach] Using Hashing - O(n*(m^2)) Time and O(n*m) Space---------------------------------------

# Python program to check if there exists a submatrix
# with all 1s at the corners using Simple Hashing

# def ValidCorner(mat):

#     rows = len(mat)
#     cols = len(mat[0])

#     # Hash set to store pairs of columns having 1 in a row
#     seen = set()

#     # Iterate through each row
#     for i in range(rows):

#         # Check all column pairs where cell is 1
#         for col1 in range(cols - 1):
#             if mat[i][col1] == 0:
#                 continue

#             for col2 in range(col1 + 1, cols):
#                 if mat[i][col2] == 0:
#                     continue

#                 # Form a unique key from column pair
#                 key = str(col1) + "," + str(col2)

#                 # If this pair seen before → rectangle exists
#                 if key in seen:
#                     return True

#                 # Otherwise store it
#                 seen.add(key)
#                 print(seen)

#     # No rectangle found
#     return False


# # Driver code
# if __name__ == "__main__":

#     mat = [
#         [1, 0, 0, 1, 0],
#         [0, 0, 1, 0, 1],
#         [0, 0, 0, 1, 0],
#         [1, 0, 1, 0, 1]
#     ]

#     if ValidCorner(mat):
#         print("true")
#     else:
#         print("false")





