# from collections import deque

# def kBitFlips(arr, k):
#     n = len(arr)
#     res = 0
    
#     q = deque(arr[:k])
#     j = k
    
#     print(sum(q))
#     while q and j < n:
#         print(q, j)
#         i = 0
#         while q[i] == 1 and i < k and j < n:
#             print("1eeeeeee")
#             q.popleft()
#             q.append(arr[j])
#             j += 1
#         print("qqq", q)
#         if len(q) < k and sum(q) < len(q):
#             print("kame")
#             return -1
        
#         if len(q) < k and sum(q) == len(q):
#             print("kame 1111111")
#             return res
        
#         for z in range(k):
#             print("tabdil", z)
#             if q[z] == 0:
#                 q[z] = 1
#             else:
#                 q[z] = 0        
#         print("baad tabdil", q, res)
                
#         if sum(q) == k:
#             print("yekeeeee", j)
#             res += 1
#             if j + k <= n:
#                 q = deque(arr[j:j + k])
#                 j = j + k
#             else:
#                 while j < n and arr[j] == 1:
#                     j += 1
#                 break
#             print("hamash 1111",j)
#         else:
#             res += 1
    
#     print("nahayii", j, q)
#     if j < n or q:
#         return -1 
               
#     return res


# arr = [0, 0, 0, 1, 0, 1, 0, 1, 1]
# k = 3
# print(kBitFlips(arr, k))

# Python3 code to count minimum no.
# of flips required such that
# every substring of length K
# contain at least one '1'.

# Function to count min flips
from collections import deque


def CountMinFlips(arr, k):
    n = len(arr)
    flip_count = 0
    flips = deque()
    operations = 0

    for i in range(n):
        print("i", i)
        # Remove expired flips
        if flips and flips[0] == i:
            print("aval")
            flips.popleft()
            flip_count -= 1

        # If current bit is 0 after flip effect
        if (arr[i] + flip_count) % 2 == 0:
            print("dovom")
            if i + k > n:
                return -1  # Not enough space to flip
            flips.append(i + k)
            flip_count += 1
            operations += 1
        print("enteha", flips, flip_count, operations)

    return operations



# Driver code
arr = [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]
k = 3
print(CountMinFlips(arr, k))
