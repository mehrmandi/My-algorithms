import heapq
def count_less_equal(m, n, x):
    count = 0
    for i in range(1, m + 1):
        count += min(n, x // i)
    return count


def find_kth_smallest(m, n, k):
    left, right = 1, m * n
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(m, n, mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


# Example usage:
m, n, k = 3, 3, 5
print(find_kth_smallest(m, n, k))  # Output: 3


# Python program to find Kth Smallest
# Number in Multiplication Table
# [Better Approach] Using Max Heap - O(m*n * log(k)) time and O(k) space------------------------


# def kthSmallest(m, n, k):
#     pq = []

#     # Check all combinations
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):

#             # If size of heap is less
#             # than k.
#             if len(pq) < k:
#                 heapq.heappush(pq, -(i * j))

#             # Else if current value is
#             # less than heap top.
#             elif i * j < -pq[0]:
#                 heapq.heappop(pq)
#                 heapq.heappush(pq, -(i * j))

#     return -pq[0]


# if __name__ == "__main__":
#     m = 3
#     n = 3
#     k = 5
#     print(kthSmallest(m, n, k))
