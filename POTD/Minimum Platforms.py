
# def minPlatform(arr, dep):
#     n = len(arr)
#     tup = list(zip(arr, dep))
#     sorted_tup = sorted(tup, key=lambda x: x[0])
#     dp = [1 for _ in range(n)]
#
#
#
#     for i in range(1, n):
#         for j in range(i):
#             if sorted_tup[i][0] <= sorted_tup[j][1]:
#                 dp[i] += 1
#
#     return max(dp)

# [Expected Approach 1] Using Sorting and Two Pointers - O(n log(n)) time and O(1) space---------------------------------
# def minPlatform(arr, dep):
#     n = len(arr)
#     res = 0

#     arr.sort()
#     dep.sort()

#     j = 0

#     cnt = 0

#     for i in range(n):
#         while j < n and dep[j] < arr[i]:
#             cnt -= 1
#             j += 1
#         cnt += 1

#         res = max(res, cnt)

#     return res


# # arr = [900, 940, 950, 1100, 1115, 1116]
# # dep = [910, 1200, 1120, 1110, 1159, 1159]
# arr = [1000, 935, 1100]
# dep = [1200, 1240, 1130]

# print(minPlatform(arr, dep))


# Python program to find minimum Platforms Required
# for Given Arrival and Departure Times

# Function to find the minimum
# number of platforms required

# Time Complexity: O(n + k), where n is the number of trains and k is the maximum value present in the arrays.-------------------------
# Auxiliary space: O(k), where k is the maximum value present in both the arrays.-------------------------------------------
def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Find the max Departure time
    maxDep = max(dep)

    # Create a list to store the count of trains at each
    # time
    v = [0] * (maxDep + 2)

    # Increment the count at the arrival time and decrement
    # at the departure time
    for i in range(n):
        v[arr[i]] += 1
        v[dep[i] + 1] -= 1

    count = 0

    # Iterate over the list and keep track of the maximum
    # sum seen so far
    for i in range(maxDep + 2):
        count += v[i]
        res = max(res, count)

    return res


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))
