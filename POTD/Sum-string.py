# def sum_string(s):
#     n = len(s)
#     if n == 0:
#          return False
     
     
#     prev1, prev2 = 0, 0
    
#     for i in range(1, n - 1):
#         prev1 = int(s[:i])
#         for j in range(i + 1, n):
#             prev2_str = s[i:j]
#             if prev2_str[0] == "0":
#                 break
#             else:
#                 prev2 = int(prev2_str)
#                 k = j
#                 numbers = 2
#                 while k < n + 1:
#                     if k == n and numbers > 2:
#                         return True
#                     sum_two = str(prev1 + prev2)
#                     m = len(sum_two)
                    
#                     if s[k : k + m] == sum_two:
#                         prev1, prev2 = prev2, int(sum_two)
#                         k += m
#                         numbers += 1
#                     else:
#                         break
                
#         if s[:i][0] == "0":
#             break
#     return False
            
    
# s = "056"
# print(sum_string(s))

# Python program to check if a string is a
# sum-string using recursion

# Adds two numeric strings and returns
# the sum as string



def addStrings(num1, num2):

    if len(num1) < len(num2):
        num1, num2 = num2, num1

    len1 = len(num1)
    len2 = len(num2)
    sum = ""
    carry = 0

    # Add from least significant digits
    for i in range(len2):
        d1 = ord(num1[len1 - 1 - i]) - ord('0')
        d2 = ord(num2[len2 - 1 - i]) - ord('0')
        digit = (d1 + d2 + carry) % 10
        carry = (d1 + d2 + carry) // 10
        sum = chr(digit + ord('0')) + sum

    # Add remaining digits of num1
    for i in range(len2, len1):
        d = ord(num1[len1 - 1 - i]) - ord('0')
        digit = (d + carry) % 10
        carry = (d + carry) // 10
        sum = chr(digit + ord('0')) + sum

    # Add remaining carry
    if carry:
        sum = chr(carry + ord('0')) + sum

    return sum

# Recursively checks if the string from index
# start is a valid sum-sequence


def checkSequence(s, start, len1, len2):
    part1 = s[start:start + len1]
    part2 = s[start + len1:start + len1 + len2]
    expectedSum = addStrings(part1, part2)

    sumLen = len(expectedSum)

    # If sum length exceeds remaining string,
    # return false
    if start + len1 + len2 + sumLen > len(s):
        return False

    # If the sum matches the next part in string
    if expectedSum == s[start + len1 + len2:
                        start + len1 + len2 + sumLen]:

        # If end is reached, return true
        if start + len1 + len2 + sumLen == len(s):
            return True

        # Recur for next pair: part2 and expectedSum
        return checkSequence(s, start + len1, len2, sumLen)

    # Sum does not match the next segment
    return False

# Function to check if a string is a sum-string


def isSumString(s):
    n = len(s)

    # Try all combinations of first two parts
    for len1 in range(1, n):
        for len2 in range(1, n - len1):
            if checkSequence(s, 0, len1, len2):
                return True

    return False


# Driver Code
if __name__ == "__main__":
    s = "12243660"
    print("true" if isSumString(s) else "false")



