# [Naive Approach] Using 2 Nested Loops – O(n^2) Time and O(1) Space------------------------------
# Function to find the maximum XOR
# def maxXor(arr):
#     res = 0

#     # Generate all possible pairs
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             res = max(res, arr[i] ^ arr[j])
#     return res


# if __name__ == "__main__":
#     arr = [26, 100, 25, 13, 4, 14]
#     print(maxXor(arr))


# [Expected Approach – 2] – Using Trie – O(n * log m) Time and O(n * log m) Space


# Function to find the maximum XOR
# def maxXor(arr):
#     res = 0
#     mask = 0

#     # to store all unique bits
#     s = set()

#     for i in range(30, -1, -1):

#         # set the i-th bit in mask
#         mask |= 1 << i
#         print("mask", mask)

#         for num in arr:

#             # keep prefix of all elements
#             # till the i-th bit
#             s.add(num & mask)
#             print("s", s)

#         print("res, (1 << i)", res)
#         cur = res | (1 << i)

#         for prefix in s:
#             if cur ^ prefix in s:
#                 res = cur
#                 break

#         s.clear()

#     return res


# if __name__ == "__main__":
#     arr = [26, 100, 25, 13, 4, 14]
#     print(maxXor(arr))


# [Expected Approach – 2] – Using Trie – O(n * log m) Time and O(n * log m) Space-------------------------


# Python program to find the maximum
# XOR n of two elements in an array
# using Trie data structure


class Node:
    def __init__(self):
        self.one = None
        self.zero = None


class Trie:
    def __init__(self):
        self.root = Node()

    # Function to insert in Trie
    def insert(self, n):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1

            # Check if the bit is 0
            if bit == 0:
                if not curr.zero:
                    curr.zero = Node()
                curr = curr.zero

            # Else if bit is 1
            else:
                if not curr.one:
                    curr.one = Node()
                curr = curr.one

    # Function to find element having
    # the maximum XOR with value n
    def findXOR(self, n):
        curr = self.root
        res = 0

        for i in range(31, -1, -1):
            bit = (n >> i) & 1

            # if the bit is 0
            if bit == 0:

                # if set bit is present
                if curr.one:
                    curr = curr.one
                    res += 1 << i
                else:
                    curr = curr.zero

            # Else if bit is 1
            else:

                # if unset bit is present
                if curr.zero:
                    curr = curr.zero
                    res += 1 << i
                else:
                    curr = curr.one
        return res


# Function to find the maximum XOR
def maxXor(arr):
    res = 0
    t = Trie()

    # insert the first element in trie
    t.insert(arr[0])

    for i in range(1, len(arr)):
        res = max(t.findXOR(arr[i]), res)
        t.insert(arr[i])
    return res


if __name__ == "__main__":
    arr = [26, 100, 25, 13, 4, 14]
    print(maxXor(arr))
