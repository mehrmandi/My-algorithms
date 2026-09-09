# Given a number n, find a number in the range from 1 to n such that its digit sum is maximum. If there are multiple such numbers, return the largest of them.

# Optimized Candidate Generation - O(log n) Time and O(log n) Space

def numChecker(n, newN, res):
    # Convert n into a string to easily access its digits
    s = str(n)
    d = len(s)

    # Calculate the digit sum of n
    totalSum = 0

    for c in s:
        totalSum += int(c)

    # Initially, n itself is the answer
    ans = n
    bestSum = totalSum

    # p represents the place value of the current digit
    p = 1

    # Sum of the current digit and all digits to its right
    suffixSum = 0

    # Traverse digits from right to left
    for i in range(d - 1, -1, -1):
        digit = int(s[i])

        # Include the current digit in the suffix sum
        suffixSum += digit

        # We can decrease the current digit only if it is greater than 0
        if digit > 0:

            # Form the candidate:
            # Keep digits to the left unchanged,
            # decrease the current digit by 1,
            # and make all digits to its right 9.
            cand = (n // (p * 10)) * (p * 10)
            cand += (digit - 1) * p
            cand += p - 1

            # Number of digits to the right
            digitsRight = d - i - 1

            # Calculate the candidate's digit sum in O(1)
            curSum = (totalSum - suffixSum
                      + (digit - 1)
                      + 9 * digitsRight)

            # Update the answer if this candidate has:
            # 1. A larger digit sum, or
            # 2. The same digit sum but a larger value
            if curSum > bestSum or (curSum == bestSum and cand > ans):
                bestSum = curSum
                ans = cand

        # Move to the next digit position
        p *= 10

    return ans
    

    
n = 521
print(findMax(n))
