from collections import deque


def catch_thieves_fast(arr, k):
    police = deque()
    thieves = deque()
    caught = 0

    for i, val in enumerate(arr):
        if val == 'P':
            police.append(i)
        elif val == 'T':
            thieves.append(i)

    while police and thieves:
        if abs(police[0] - thieves[0]) <= k:
            caught += 1
            police.popleft()
            thieves.popleft()
        elif thieves[0] < police[0]:
            thieves.popleft()
        else:
            police.popleft()

    return caught


# [Expected Approach] Using Two Pointers - O(n) Time and O(1) Space


# Python program to find the maximum number of thieves caught

# Returns the maximum number of thieves
# that can be caught using two pointers
# def catchThieves(arr, k):
#     n = len(arr)

#     # Two pointers for policemen and thieves
#     i, j = 0, 0
#     count = 0

#     while i < n and j < n:

#         # Move i to the next policeman
#         while i < n and arr[i] != 'P':
#             i += 1

#         # Move j to the next thief
#         while j < n and arr[j] != 'T':
#             j += 1

#         # If both policeman and thief exist
#         # and are within range k
#         if i < n and j < n and abs(i - j) <= k:

#             # Catch the thief
#             count += 1

#             # Move to the next policeman
#             i += 1

#             # Move to the next thief
#             j += 1

#         # If the thief is too far left,
#         # move the thief pointer
#         elif j < n and j < i:
#             j += 1

#         # If the policeman is too far left,
#         # move the policeman pointer
#         elif i < n and i < j:
#             i += 1

#     return count


# if __name__ == "__main__":
#     k = 1
#     arr = ['P', 'T', 'T', 'P', 'T']
#     print(catchThieves(arr, k))
