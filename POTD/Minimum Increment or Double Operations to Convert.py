# Given an array arr[]. Initially, you have another array containing only 0s.
# In one operation, you may either:

# Choose any one element and increase its value by 1, or
# Double the values of all elements in the array simultaneously.
# Find the minimum number of operations required to transform the initial all-zero array into the given array arr[].

# Bit Manipulation - O(n × log m) Time and O(1) Space


def countMinOperations(arr):

    # Tracks total increment operations (set bits)
    incs = 0

    # Tracks the maximum bit length found
    maxLen = 0

    for val in arr:
        len = 0

        while val > 0:

            # An odd number (lowest bit set) implies an increment operation
            if (val & 1) != 0:
                incs += 1
            len += 1
            # Shift right to inspect the next bit
            val >>= 1

        maxLen = max(maxLen, len)

    # Total doubling operations equals (max bit length - 1)
    dbls = max(0, maxLen - 1)

    return incs + dbls
    
 
arr = [2, 3]
print(countMinOperations(arr))

    
