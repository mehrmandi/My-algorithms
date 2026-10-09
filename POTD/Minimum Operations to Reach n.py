# Given a number n. Find the minimum number of operations required to reach n starting from 0. You have two operations available:

# Double the number
# Add one to the number


# Bit Manipulation - O(logn) Time and O(1) Space


def minOperation(n):
    # Tracks total increment operations (set bits)
    incs = 0
    len = 0
    
    while n > 0:
        # An odd number (lowest bit set) implies an increment operation
        if (n & 1) != 0:
            incs += 1
            
        len += 1
        
        # Shift right to inspect the next bit
        n >>= 1
    
    # Total doubling operations equals (max bit length - 1)    
    dbls = max(0, len - 1)
    
    return incs + dbls
        
    
n = 15
print(minOperation(n))     
            
            
