import heapq
def subArraySum(arr, k):
    res = []
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            res.append(sum(arr[i:j + 1]))
    
    res.sort(reverse=True)        
    return res[k - 1]


arr = [3, 2, 1]
k = 2
print(subArraySum(arr, k))


# [Expected Approach] - Using Min Heap - O(n2 * log k) Time and O(k) Space


# Function to calculate Kth largest element
# in contiguous subarray sum
# def kthLargest(arr, k):
#     n = len(arr)

#     # array to store prefix sums
#     sum = [0] * (n + 1)
#     sum[0] = 0
#     sum[1] = arr[0]
#     for i in range(2, n + 1):
#         sum[i] = sum[i - 1] + arr[i - 1]

#     # min heap
#     pq = []

#     # loop to calculate the contiguous subarray
#     # sums position-wise
#     for i in range(1, n + 1):

#         # loop to traverse all positions that
#         # form contiguous subarray
#         for j in range(i, n + 1):

#             # calculates the contiguous subarray
#             # sums from j to i index
#             x = sum[j] - sum[i - 1]

#             # if queue has less than k elements,
#             # then simply push it
#             if len(pq) < k:
#                 heapq.heappush(pq, x)
#             else:

#                 # it the min heap has equal to
#                 # k elements then just check
#                 # if the largest kth element is
#                 # smaller than x then insert
#                 # else its of no use
#                 if pq[0] < x:
#                     heapq.heapreplace(pq, x)

#     # the top element will be then kth
#     # largest element
#     return pq[0]


# # Driver's code
# if __name__ == "__main__":
#     arr = [20, -5, -1]
#     k = 3

#     # Function call
#     print(kthLargest(arr, k))
