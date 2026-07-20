# [Naive Approach] Using Nested Loop - O(n^3) Time and O(1) Space-----------------------

# def substringsSum(s):
#     n = len(s)
#     sum = 0
    
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             sub = s[i:j]
#             sum += int(sub)
            
            
#     return sum


# s = "222"
# print(substringsSum(s))


# [Naive Approach] Using Nested Loop - O(n^2) Time and O(1) Space--------------------------


# def sumSubstrings(s):
#     # Final answer to store the sum of all substrings
#     ans = 0
#     # Length of the input string
#     n = len(s)

#     for i in range(n):
#         # Temporary variable to hold current substring value
#         temp = 0

#         for j in range(i, n):
#             # Shift the previous value by one digit to the left
#             temp *= 10
#             # Add current digit to form the number
#             temp += int(s[j])
#             # Add the current substring number to the answer
#             ans += temp
#     return ans


# if __name__ == "__main__":
#     s = "6759"
#     # Output the sum of all substrings
#     print(sumSubstrings(s))


# [Better Approach] Using Dynamic Programming - O(n) Time and O(n) Space----------------------------

# Python3 program to print
# sum of all substring of
# a sber represented as
# a string
# def sumSubstrings(s):
#     n = len(s)

#     # allocate memory equal
#     # to length of string
#     sumofdigit = []

#     # initialize first value
#     # with first digit
#     sumofdigit.append(int(s[0]))
#     res = sumofdigit[0]

#     # loop over all
#     # digits of string
#     for i in range(1, n):
#         si = int(s[i])

#         # update each sumofdigit
#         # from previous value
#         sumofdigit.append((i + 1) *
#                           si + 10 * sumofdigit[i - 1])

#         # add current value
#         # to the result
#         res += sumofdigit[i]

#     return res


# # Driver Code
# if __name__ == '__main__':
#   s = "6759"
#   print(sumSubstrings(s))


# [Expected Approach] Within Constant Space - O(n) Time and O(n) Space------------------------------


# Python3 program to print sum of all substring of
# a stdber represented as a string

# Returns sum of all substring of std
def sumSubstrings(s):

    # Initialize result
    sum = 0

    # Here traversing the array in reverse
    # order.Initializing loop from last
    # element.
    # mf is multiplying factor.
    mf = 1
    for i in range(len(s) - 1, -1, -1):

        # Each time sum is added to its previous
        # sum. Multiplying the three factors as
        # explained above.
        # int(s[i]) is done to convert char to int.
        sum = sum + (int(s[i])) * (i + 1) * mf

        # Making new multiplying factor as
        # explained above.
        mf = mf * 10 + 1

    return sum


# Driver Code
if __name__ == '__main__':
    s = "123"
    print(sumSubstrings(s))
