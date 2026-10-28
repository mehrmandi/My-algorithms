# Consider a string s formed by concatenating the decimal representations of all positive integers in order:

# s = "12345678910111213141516171819202122232425262728293031..."

# Given an integer n, find the nth character(1-based indexing) in the string s.

# Digit Grouping and Extraction - O(log n) Time and O(1) Space

def nthCharacter(n):
    # Find the number of digits in the number that contains the nth character
    digits = 1
    digits_count = 9
    
    # Keep subtracting the count of digits in each group until we find the group that contains the nth character
    while n > digits_count:
        n -= digits_count
        digits += 1
        digits_count = 10 ** (digits - 1) * digits * 9
    
    # Calculate the count of numbers with the current number of digits and the position of the digit within that number
    count = (n - 1) // digits 
    units = (n - 1)% digits
    
    # Calculate the actual number that contains the nth character
    num = 10 ** (digits - 1) + count
    
    # Calculate the divisor to extract the specific digit from the number instead of converting the number to a string
    div = 10 ** (digits - units - 1)

    # Extract the specific digit from the number using integer division and modulo operations
    digit = (num // div) % 10
    
    return str(digit)



    
n = 25874126587
print(nthCharacter(n))