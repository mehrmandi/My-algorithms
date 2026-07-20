#import sys


# def helper(s):
#     n = len(s)
#     if n == 2:
#         if int(s) % 13 == 0:
#             return True
#         else:
#             return False
#     last = int(s[-1])
#     rem = int(s[:n - 1])
#     new_s = str((last * 4) + rem)
#     return helper(new_s)
    


# def divisibleByThirteen(s):
#     sys.set_int_max_str_digits(0)
#     n = len(s)
#     if n < 2:
#         return False
#     return helper(s)



 
# Time Complexity: O(n), n is length of s---------------------------------------
# Auxiliary Space: O(1)
def is_divisible_by_13(s):
    remainder = 0
    for ch in s:
        remainder = (remainder * 10 + int(ch)) % 13
    return remainder == 0

    
s = "245115687"
print(is_divisible_by_13(s))