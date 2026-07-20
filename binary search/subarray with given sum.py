# def subarray_sum(arr, n, sum):
#     last = 0
#     start = 0
#     currsum = 0
#     flag = False
#     res = []

#     print(arr)

#     # Iterate over the array
#     for i in range(n):
#         # Store sum up to current element
#         currsum += arr[i]
#         print("i", i)
#         print("cursum1", currsum)

#         # Check if current sum is greater than or equal to given number
#         if currsum >= sum:
#             last = i
#             print("last", last)

#             # Start from starting index till current index
#             while sum < currsum and start < last:
#                 print("cursum2", currsum)
#                 # Subtract the element from left
#                 currsum -= arr[start]
#                 start += 1
#                 print("start", start)

#             # If current sum becomes equal to given number
#             if currsum == sum:
#                 res.append(start + 1)
#                 res.append(last + 1)
#                 flag = True
#                 break

#     # If no subarray is found, store -1 in result
#     if not flag:
#         res.append(-1)

#     # Return the result
#     return res


# # Driver Code
# arr = [15, 2, 4, 8, 9, 5, 10, 23]
# n = len(arr)
# sum = 23
# res = subarray_sum(arr, n, sum)
# for i in res:
#     print(i, end=" ")
    
# [Expected Approach] Sliding Window - O(n) Time and O(1) Space-----------------------------------------------


def subarraySum(arr, target):
    # Initialize window
    s, e = 0, 0
    res = []

    curr = 0
    for i in range(len(arr)):
        curr += arr[i]

        # If current sum becomes more or equal,
        # set end and try adjusting start
        if curr >= target:
            e = i

            # While current sum is greater,
            # remove starting elements of current window
            while curr > target and s < e:
                curr -= arr[s]
                s += 1

            # If we found a subarray
            if curr == target:
                res.append(s + 1)
                res.append(e + 1)
                return res

    # If no subarray is found
    return [-1]


if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    res = subarraySum(arr, target)

    print(" ".join(map(str, res)))
