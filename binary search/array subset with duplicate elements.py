# def isSubset(a, b):
#     visited = [False for _ in range(len(a))]
#     for i in range(len(b)):
#         found = False
#         for j in range(len(a)):
#             print(j, visited[j])
#             if a[j] == b[i] and visited[j] == False:
#                 print(i, a[j], j, b[i])
#                 visited[j] = True
#                 found = True
#                 break
#
#         if found == False:
#             print("no")
#             return "No"
#
#     # If all elements are found, return true
#     return "Yes"


def is_subset(a, b):

    # Sort both arrays in ascending order
    a.sort()
    b.sort()

    i = 0
    j = 0

    # Traverse both arrays using two pointers
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            # Element in arr1 is smaller, move to the next element in arr1
            i += 1
        elif a[i] == b[j]:
            # Element found in both arrays, move to the next element in both arrays
            i += 1
            j += 1
        else:
            # Element in arr2 not found in arr1, not a subset
            return "No"

    # If we have traversed all elements in arr2, it is a subset
    return "Yes"

a = [11, 7, 1, 13, 21 ,3 ,3]
b = [11, 3, 7, 1, 7]

print(is_subset(a, b))
