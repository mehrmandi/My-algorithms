# [Expected Approach for Small Range] Using Count Array and Prefix Sum - O(n + m + max(b[i])) Time and O(max(b[i])) Space


def countingElement(a, b):
    n = len(a)
    m = len(b)

    # to store the result
    res = [0] * n
    maxi = max(b)
    # to store frequency of elements in b[]
    cnt = [0] * (maxi + 1)

    for i in range(m):
        cnt[b[i]] += 1
        
    print("aval", cnt)

    # transform cnt[] to prefix sum array
    for i in range(1, (maxi + 1)):
        cnt[i] += cnt[i - 1]
    
    print("prefix", cnt)

    # loop for each element of a[]
    for i in range(n):
        res[i] = cnt[min(a[i], maxi)]

    return res
    
    


a = [4, 8, 7, 5, 1]
b = [4, 48, 3, 0, 1, 1, 5]
print(countingElement(a, b))


# Better Approach - 1] Using Sorting - O((n + m) * log m) Time and O(n) Space


# to perform the binary search
# def binarySearch(arr, x):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = low + (high - low) // 2
#         if arr[mid] <= x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low

# # to store the result


# def countEleLessThanOrEqual(a, b):
#     n = len(a)
#     m = len(b)

#     # to store the result
#     res = [0] * n

#     # sort the array b[]
#     b.sort()

#     # outer loop for each element of a[]
#     for i in range(n):
#         res[i] = binarySearch(b, a[i])
#     return res


# if __name__ == "__main__":
#     a = [1, 2, 3, 4, 7, 9]
#     b = [0, 1, 2, 1, 1, 4]
#     result = countEleLessThanOrEqual(a, b)
#     for i in result:
#         print(i, end=" ")
