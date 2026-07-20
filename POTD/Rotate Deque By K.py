# from collections import deque

# # Function to reverse elements in
# # the list between indices start and end


# def reverseList(arr, start, end):
#     while start < end:

#         # Swap elements at start and end
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1

# # Function to rotate the deque by k
# # positions using Reversal Algorithm


# def rotateDeque(dq, type, k):
#     n = len(dq)

#     # If deque is empty, nothing to rotate
#     if n == 0:
#         return

#     # Use modulo to avoid unnecessary full rotations
#     k = k % n
#     if k == 0:
#         return

#     # Convert deque to list for index-based operations
#     arr = list(dq)

#     # Right rotation (clockwise)
#     if type == 1:
#         reverseList(arr, 0, n - 1)
#         reverseList(arr, 0, k - 1)
#         reverseList(arr, k, n - 1)

#     # Left rotation (anti-clockwise)
#     elif type == 2:
#         reverseList(arr, 0, k - 1)
#         reverseList(arr, k, n - 1)
#         reverseList(arr, 0, n - 1)

#     dq.clear()
#     dq.extend(arr)


# if __name__ == "__main__":
#     dq = deque([1, 2, 3, 4, 5, 6])
#     type = 1
#     k = 2
#     rotateDeque(dq, type, k)

#     for val in dq:
#         print(val, end=" ")

