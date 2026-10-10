# Given a simple weighing scale with two pans, a target weight b, and a set of weights where each weight is a distinct power of a, find if the scale can be balanced such that:

# b + (some powers of a) = (some other powers of a)

# Note: Exactly one weight is available for each power of a, so each power can be used at most once.

# Greedy Reverse - O(log n) Time and O(1) Space

def balancePan(a, b):
    while b > 0:
        rem = b % a
        
        print(rem, b)

        # Remainder 0 or 1 means no carry is needed.
        if rem == 0 or rem == 1:
            b //= a

        # Remainder a - 1 means use one weight on opposite side and carry 1.
        elif rem == a - 1:
            b = b // a + 1

        # Any other remainder cannot be balanced.
        else:
            return False

    return True
            

    
a = 3
b = 15
print(balancePan(a, b))
