# Given an array arr[] of size n, find the length of the Longest Increasing Subsequence(LIS) i.e., the longest possible subsequence in which the elements of the subsequence are sorted in strictly increasing order.

# Using Binary Search - O(n Log n) Time and O(n) Space
def lIS(arr):
    n = len(arr)
    ans = []

    # Initialize the answer list with the
    # first element of arr
    ans.append(arr[0])

    for i in range(1, n):
        if arr[i] > ans[-1]:
            # If the current number is greater
            # than the last element of the answer
            # list, it means we have found a
            # longer increasing subsequence.
            # Hence, we append the current number
            # to the answer list.
            ans.append(arr[i])
        else:
            # If the current number is not
            # greater than the last element of
            # the answer list, we perform
            # a binary search to find the smallest
            # element in the answer list that
            # is greater than or equal to the
            # current number.
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < arr[i]:
                    low = mid + 1
                else:
                    high = mid
            # We update the element at the
            # found position with the current number.
            # By doing this, we are maintaining
            # a sorted order in the answer list.
            ans[low] = arr[i]

    # The length of the answer list
    # represents the length of the
    # longest increasing subsequence.
    return len(ans)


arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(lIS(arr))
