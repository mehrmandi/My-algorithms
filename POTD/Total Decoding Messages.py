# # Python program to count decoding ways of a digit string
# # using recursion.
#
# # Helper function to recursively calculate decoding ways
# def decodeHelper(digits, index):
#     n = len(digits)
#
#     # Base case: If we reach the end of the string,
#     # return 1 as it signifies a valid decoding.
#     if index >= n:
#         return 1
#
#     ways = 0
#
#     # Single-digit decoding: check if current digit is not '0'.
#     if digits[index] != '0':
#         ways = decodeHelper(digits, index + 1)
#
#     # Two-digit decoding: check if next two digits are valid.
#     if (index + 1 < n and
#         ((digits[index] == '1' and digits[index + 1] <= '9') or
#          (digits[index] == '2' and digits[index + 1] <= '6'))):
#
#         ways += decodeHelper(digits, index + 2)
#
#     return ways
#
# # Function to count decoding ways for the entire string
#
#
# def countWays(digits):
#     return decodeHelper(digits, 0)
#---------------------------------------------------------------------------
# def countWays(digits):
#     n = len(digits)
#
#     # If the string is empty or starts with '0',
#     # there are no valid decodings.
#     if n == 0 or digits[0] == '0':
#         return 0
#
#     # two variables to store the previous two results.
#     prev1, prev2 = 1, 0
#
#     for i in range(1, n + 1):
#         current = 0
#         # Check for valid single-digit decoding
#         if digits[i - 1] != '0':
#             current += prev1
#         # Check for valid two-digit decoding
#         # (previous digit and current digit form a valid number between 10 and 26)
#         if i > 1:
#             two_digit = (int(digits[i - 2]) * 10 + int(digits[i - 1]))
#             if 10 <= two_digit <= 26:
#                 current += prev2
#
#         # Update prev1 and prev2 for the next iteration.
#         prev2 = prev1
#         prev1 = current
#     return prev1

# -----------------------------------------------------------------------------------





digits = "022544879620"
print(countWays(digits))
