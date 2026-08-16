# Given an integer array arr[], determine the minimum possible product that can be obtained by multiplying the elements of any non-empty subset of the array.

# Mathematical Observation - O(n) Time and O(1) Space

def minProd(arr):
    last_neg = float('-inf')
    min_pos = float('inf')
    neg_count = 0
    product = 1
    has_zero = False

    # Iterate through the array to calculate the product, count of negative numbers, and track the last negative number and minimum positive number.
    for num in arr:
        if num == 0:
            has_zero = True
        elif num < 0:
            neg_count += 1
            last_neg = max(last_neg, num)
            product *= num
        else:
            min_pos = min(min_pos, num)
            product *= num

    # Handle edge cases based on the count of negative numbers and the presence of zero.
    if neg_count == 0:
        return 0 if has_zero else min_pos

    if neg_count % 2 == 0:
        return product // last_neg

    return product
            
    
arr = [-3, -3, -1, 2, -2, -5, 0, 5]

print(minProd(arr))
