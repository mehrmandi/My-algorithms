# [Better Approach 1] Using Merge Step of Merge Sort - O(m + n) Time and O(m + n) Space--------------
# def kthElement(a, b, k):
#     n = len(a)
#     m = len(b)
#     res = []
#     i = 0
#     j = 0
    
#     while i < n and j < m:
#         if a[i] <= b[j]:
#             res.append(a[i])
#             i += 1
#         else:
#             res.append(b[j])
#             j += 1
            
#     while i < n:
#         res.append(a[i])
#         i += 1
        
#     while j < m:
#         res.append(b[j])
#         j += 1
        
#     return res[k - 1]

# a = [2, 3, 6, 7, 9]
# b = [1, 4, 8, 10]
# k = 5
# print(kthElement(a, b, k))

# [Expected Approach] Using Binary Search - O(log min(n, m)) Time and O(1) Space-------------
def kthElement(a, b, k):
    n = len(a)
    m = len(b)

    # if a[] has more elements, then call kthElement
    # with reversed parameters
    if n > m:
        return kthElement(b, a, k)

    # binary Search on the number of elements we can
    # include in the first set from a[]
    lo = max(0, k - m)
    hi = min(k, n)
    print(lo, hi)

    while lo <= hi:
        mid1 = (lo + hi) // 2
        print("mid1", mid1)
        mid2 = k - mid1
        print("mid2", mid2)

        # find elements to the left and right of
        # partition in a[]
        l1 = (mid1 == 0 and float('-inf') or a[mid1 - 1])
        r1 = (mid1 == n and float('inf') or a[mid1])
        

        # find elements to the left and right of
        # partition in b[]
        l2 = (mid2 == 0 and float('-inf') or b[mid2 - 1])
        r2 = (mid2 == m and float('inf') or b[mid2])
        
        print("l1, l2, r1, r2", l1, l2, r1, r2)

        # if it is a valid partition
        if l1 <= r2 and l2 <= r1:
            print("iffff")

            # find and return the maximum of l1 and l2
            return max(l1, l2)

        # check if we need to take lesser elements
        # from a[]
        if l1 > r2:
            hi = mid1 - 1

        # check if we need to take more elements
        # from a[]
        else:
            lo = mid1 + 1

    return 0


if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(kthElement(a, b, k))
