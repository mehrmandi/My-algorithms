# def andInRange(l, r):
#     shift = 0
#     while l < r:
#         l >>= 1
#         r >>= 1
#         shift += 1
#         print(shift, l, r)
#     return l << shift

# l = 5
# r = 8
# print(andInRange(l, r))


import math

# [Expected Approach - 1] masking - O(log r) Time and O(1) Space--------------------
def andInRange(l, r):
    if l == r:
        return l
    x = l ^ r
    msb = x.bit_length()  # position of highest differing bit
    mask = ~((1 << (msb)) - 1)
    return l & mask


l = 8
r = 13
print(andInRange(l, r))


# [Expected Approach - 1] Checking For All Bits - O(log r) Time and O(1) Space-----------------

# def andInRange(l, r):
#     andInRange = 0

#     maxSetBit = int(math.log(r, 2))
#     print("aval", maxSetBit, math.log(r, 2))

#     # for each bit check if it
#     # will be set in the AND of range
#     for bit in range(maxSetBit + 1):
#         andWithR = (r & (1 << bit))
#         andWithL = (l & (1 << bit))
#         print(bit, andWithR, andWithL)

#         # if bit is set in l and r
#         if andWithR > 0 and andWithL > 0:

#             # if the numbers in range
#             # from l to r <= 2^k
#             if r - l + 1 <= (1 << bit):
#                 andInRange = andInRange | (1 << bit)
#                 print("if", andInRange)

#     return andInRange


if __name__ == "__main__":
    l, r = 10, 15
    print(andInRange(l, r))
