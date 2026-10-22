# Given a string s consisting of lowercase English letters and the character '?',

# Replace every '?' with a lowercase English letter such that the resulting string is a palindrome.
# If it is possible to form a palindrome, return the minimum possible sum of the absolute ASCII differences between every pair of adjacent characters in the resulting string.
# If it is not possible to form a palindrome, return -1.


# Two-Pointer Cost Accumulation — O(n) Time, O(1) Space

def minimumSum(s: str) -> int:
    l, r = 0, len(s) - 1
    
    # defined a variable to keep track of the previous character and the total cost
    prev = None
    cost = 0

    # use a while loop to iterate through the string from both ends towards the center
    while l <= r:
        a, b = s[l], s[r]
        
        # check if both characters are not '?' and are different, in which case it is impossible to form a palindrome
        if a != '?' and b != '?' and a != b:
            return -1

        # determine the character to use for the current pair of characters, preferring the non-'?' character if one exists
        ch = a if a != '?' else b

        # if the chosen character is not '?', calculate the cost of changing from the previous character to the current character and update the previous character
        if ch != '?':
            if prev is not None:
                cost += abs(ord(ch) - ord(prev))
            prev = ch

        l += 1
        r -= 1

        return cost * 2


s = "???"
print(minimumSum(s))
