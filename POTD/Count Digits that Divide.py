# Time Complexity: O(d) where d is the number of digits in a number.
# Auxiliary Space: O(1)

# Return the number of digits
# that divides the number.


def countDigit(n):
    temp = n
    count = 0
    while temp != 0:

        # Fetching each digit
        # of the number
        d = temp % 10
        temp //= 10

        # Checking if digit is greater
        # than 0 and can divides n.
        if d > 0 and n % d == 0:
            count += 1
    return count
        
        


n = 120
print(countDigit(n))