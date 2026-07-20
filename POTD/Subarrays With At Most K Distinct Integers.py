from collections import defaultdict

# def subarrayKDistinct(arr, k):
#     n = len(arr)
#     count = {}
#     left, right = 0, 0
#     res = 0
#     sub_count = 0

#     while right < n:
#         count[arr[right]] = count.get(arr[right], 0) + 1
#         sub_count += 1

#         while len(count) > k:
#             count[arr[left]] -= 1
#             sub_count -= 1

#             if count[arr[left]] == 0:
#                 del count[arr[left]]

#             left += 1

#         res += sub_count
#         right += 1

#     return res


# arr = [1, 2, 1, 1, 3, 3, 4, 2, 1]
# k = 2

# print(subarrayKDistinct(arr, k))


def countAtMostK(arr, k):
    n = len(arr)
    res = 0

    # pointers to mark the left and right boundary
    left, right = 0, 0

    # frequency map
    freq = defaultdict(int)
    while right < n:
        freq[arr[right]] += 1

        # if this is a new element in the window,
        # decrement k by 1
        if freq[arr[right]] == 1:
            k -= 1

        # shrink the window until distinct element
        # count becomes <= k
        while k < 0:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                k += 1
            left += 1

        # count of subarrays ending at "right"
        # and having atmost k elements
        res += (right - left + 1)
        right += 1
    return res


if __name__ == "__main__":
    arr = [1, 2, 1, 1, 3, 3, 4, 2, 1]
    k = 2
    print(countAtMostK(arr, k))
