def commonElements(A, B, C):
    i, j, k = 0, 0, 0
    common = []

    # Iterate through three arrays while all arrays have elements
    while i < len(A) and j < len(B) and k < len(C):
        # If A[i] == B[j] == C[k], add A[i] to common elements
        if A[i] == B[j] and B[j] == C[k]:
            common.append(A[i])
            i += 1
            j += 1
            k += 1

            # Skip duplicate elements in A[]
            while i < len(A) and A[i] == A[i - 1]:
                i += 1
            # Skip duplicate elements in B[]
            while j < len(B) and B[j] == B[j - 1]:
                j += 1
            # Skip duplicate elements in C[]
            while k < len(C) and C[k] == C[k - 1]:
                k += 1

        # If A[i] < B[j], then ith element cannot be common
        elif A[i] < B[j]:
            i += 1

        # If B[j] < C[k], then jth element cannot be common
        elif B[j] < C[k]:
            j += 1
        # If C[k] is smallest, then kth element cannot be common
        else:
            k += 1

    return common


# Sample Input
A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20]z
C = [5, 20]

common = commonElements(A, B, C)

print("Common Elements:", end=" ")
for ele in common:
    print(ele, end=" ")