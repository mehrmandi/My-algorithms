def match(curr, res):
    if curr > res:
        res = curr
    return res


def setDigit(s, index, res, k):

    # Base case: If no swaps left or index reaches
    # the last character, update result
    if k == 0 or index == len(s) - 1:
        res = match(s, res)
        return res

    maxDigit = 0

    # Finding maximum digit for placing at given index
    for i in range(index, len(s)):
        maxDigit = max(maxDigit, int(s[i]))

    # If the digit at current index is already max
    if int(s[index]) == maxDigit:
        res = setDigit(s, index + 1, res, k)
        return res

    # Try swapping with the maximum digit found
    for i in range(index + 1, len(s)):

        # If max digit is found at current position
        if int(s[i]) == maxDigit:

            # Swap to get the max digit at the required index
            s = swap(s, index, i)

            # Call the recursive function to set the next digit
            res = setDigit(s, index + 1, res, k - 1)

            # Backtrack: swap the digits back
            s = swap(s, index, i)

    return res

# Function to swap characters in the string


def swap(s, i, j):

    # Convert string to list for mutation,
    # then back to string
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

# Function to find the largest number after k swaps


def findMaximumNum(s, k):
    res = s
    res = setDigit(s, 0, res, k)

    # Returning the result
    return res
    
s = "42431636"
k = 3
print(largest_number_by_swaps(s, k))
