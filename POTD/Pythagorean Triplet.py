import math

# [Expected Approach] Iterating till max element - O(max(arr)^2) Time and O(max(arr)) Space----------------------
def pythagoreanTriplet(arr):
    n = len(arr)
    maxEle = 0
    for ele in arr:
        maxEle = max(maxEle, ele)

    # Visited array to mark the elements
    vis = [False] * (maxEle + 1)

    # Marking each element of input array
    for ele in arr:
        vis[ele] = True

    # Iterate for all possible a
    for a in range(1, maxEle + 1):

        # If a is not there
        if not vis[a]:
            continue

        # Iterate for all possible b
        for b in range(1, maxEle + 1):

            # If b is not there
            if not vis[b]:
                continue

            # calculate c value to form a pythagorean triplet
            c = int(math.sqrt(a * a + b * b))

            # If c^2 is not a perfect square or c exceeds the
            # maximum value
            if (c * c) != (a * a + b * b) or c > maxEle:
                continue

            # If there exists c in the original array,
            # we have found the triplet
            if vis[c]:
                return True

    return False


# [Better Approach-2] Using Hashing - O(n^2) Time and O(n) Space--------------------------------------

# def pythagoreanTriplet(arr):
#     arr.sort()
#     n = len(arr)
#     if n < 3:
#         return False
    
#     max_quad = max(arr) ** 2

#     dp = [0 for _ in range(max_quad + 1)]
    
#     for i in range(n):
#         dp[arr[i] ** 2] += 1
        
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             c = arr[i] ** 2 + arr[j] ** 2
#             if c > max_quad:
#                 break
            
#             if dp[c] > 0:
#                 return True        
            
#     return False
        

# arr = [1, 1, 1]
# print(pythagoreanTriplet(arr))

# [Better Approach-2] Using Hashing - O(n^2) Time and O(n) Space----------------------------


# def has_pythagorean_triplet(arr):
#     n = len(arr)
#     arr = [x**2 for x in arr]  # Square each element
#     arr.sort()  # Sorting makes search easier

#     # Check if any triplet satisfies a^2 + b^2 = c^2
#     for c in range(n-1, 1, -1):  # Start from largest
#         a, b = 0, c - 1  # Two-pointer approach
#         while a < b:
#             if arr[a] + arr[b] == arr[c]:  # Found a valid triplet
#                 return True
#             elif arr[a] + arr[b] < arr[c]:
#                 a += 1  # Increase sum
#             else:
#                 b -= 1  # Decrease sum

#     return False  # No triplet found


# # Example Usage
# arr = [3, 2, 4, 6, 5]
# print(has_pythagorean_triplet(arr))  # Output: True
    

    
    