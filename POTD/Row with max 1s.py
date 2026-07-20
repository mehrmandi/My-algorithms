def rowWithMax1s(arr):
    n = len(arr)
    sum_row = 0
    row = -1
    
    for i in range(n):
        subSum = sum(arr[i])
        if subSum > sum_row:
            sum_row = subSum
            row = i
    
    return row
        
        
arr = [[0, 0], [1, 1]]

print(rowWithMax1s(arr))

# Time Complexity: O(n+m), The algorithm traverses the array from top-right to bottom-left, moving either left or down in each step. In the worst case, the algorithm will move either n times(moving down) or m times(moving left).
# Space Complexity: O(1), The algorithm uses a constant amount of extra space for variables like r, c, and max_row_index.

# Solution class that contains the method rowWithMax1s
# class Solution:

#     def rowWithMax1s(self, arr):
#         n = len(arr)  # Number of rows
#         m = len(arr[0])  # Number of columns
#         r = 0  # Start from the first row
#         c = m - 1  # Start from the last column
#         max_row_index = -1  # Track the row with the most 1s

#         # Traverse from top-right to bottom-left
#         while r < n and c >= 0:
#             if arr[r][c] == 1:  # Move left if 1 is found
#                 max_row_index = r  # Update the row with the most 1s
#                 c -= 1
#             else:
#                 r += 1  # Move down if 0 is found

#         return max_row_index  # Return the row with the most 1s
