# [Better Approach] Using Binary Search - O((n^2)*log n) Time and O(1) Space--------------------------------------------


# from bisect import bisect_left

# def countTriangles(arr):
#     n = len(arr)
#     arr.sort()
#     res = 0
#     if n < 3:
#         return res
    
#     for i in range(n - 1, 1, -1):
#         fst = arr[i]
#         for j in range(i - 1, -1, -1):
#             sec = arr[j]
#             idx = bisect_left(arr, fst  - sec + 1)
#             if j > idx:
#                 res += j - idx
                
#     return res
            
            
# arr = [1, 1, 2, 2, 2, 3]

# print(countTriangles(arr))


# [Better Approach] Using Binary Search - O((n^2)*log n) Time and O(1) Space--------------------------------------------
# from bisect import bisect_left


# def countTriangles(arr):
#     res = 0

#     # Sort the array to apply the
#     # triangle inequality efficiently
#     arr.sort()

#     # Iterate through pairs of sides (arr[i], arr[j])
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):

#             # Find the first index where the
#             # sum of two sides is not valid
#             k = bisect_left(arr, arr[i] + arr[j], j + 1)

#             # Count the number of valid third sides
#             cnt = k - j - 1
#             res += cnt

#     return res


# if __name__ == "__main__":
#     arr = [4, 6, 3, 7]
#     print(countTriangles(arr))

# [Expected Approach] Using Two Pointers Technique - O(n^2) Time and O(1) Space----------------------------------
def countTriangles(arr):
    res = 0
    arr.sort()

    # Iterate through the array, fixing
    # the largest side at arr[i]
    for i in range(2, len(arr)):

        # Initialize pointers for the two smaller sides
        left, right = 0, i - 1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                # arr[left] + arr[right] satisfies the triangle inequality,
                # so all pairs (x, right) with (left <= x < right) are valid
                res += right - left

                # Move the right pointer to check smaller pairs
                right -= 1

            else:
                # Move the left pointer to increase the sum
                left += 1

    return res


if __name__ == "__main__":
    arr = [4, 6, 3, 7]
    print(countTriangles(arr))
