# # [Expected Approach] Using HashMap - O(n) Time and O(n) Space--------------------------



# def countSubarrays(arr, k):
#     n = len(arr)
#     count = 0

#     # to store count of prefix subarrays
#     # with particular count of odd numbers
#     prefix = {0: 1}

#     # to store count of odd numbers
#     odd = 0

#     for i in range(n):

#         # if current element is odd
#         if arr[i] % 2 != 0:
#             odd += 1

#         # if count of odd numbers in
#         # subarray is k
#         if (odd - k) in prefix:
#             count += prefix[odd - k]

#         prefix[odd] = prefix.get(odd, 0) + 1

#     return count



# arr = [2, 2, 5, 6, 9, 2, 11]
# k = 3
# print(countSubarrays(arr, k))

# at most x odd elements


# [Optimal Approach] Using Subarrays with (k - 1) Odds - O(n) Time and O(1) Space------------------
def atMostX(arr, x):
    n = len(arr)

    # to store count of odd elements
    odd = 0

    ans = 0
    start = 0

    for i in range(n):

        # if current element is odd
        if arr[i] % 2 != 0:
            odd += 1

        # if count of odd elements is greater than x
        # then remove elements from the start
        while odd > x:
            if arr[start] % 2 != 0:
                odd -= 1
            start += 1

        # add the number of subarrays with at most x
        # odd elements ending at the current index
        ans += i - start + 1

    return ans

# function to find the count of subarrays with
# number of odd elements equal to k.


def countSubarrays(arr, k):
    n = len(arr)

    # find count of subarrays with at most
    # k and k - 1 odd elements
    x = atMostX(arr, k)
    y = atMostX(arr, k - 1)
    return x - y
