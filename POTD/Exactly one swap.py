# def count_repeated_letters(s):
#     letter_count = {}
#     for char in s:
#         if char.isalpha():
#             letter_count[char] = letter_count.get(char, 0) + 1

#     repeated_letters = {char: count for char,
#                         count in letter_count.items() if count > 1}
#     return repeated_letters


# def oneSwap(s):
#     n = len(s)
#     new_word = n * (n - 1) // 2
#     letter_rep = count_repeated_letters(s)
    
#     for key, val in letter_rep.items():
#         new_word -= (val * (val - 1)// 2)
    
#     if letter_rep:
#         return new_word + 1
#     else:    
#         return new_word
        
    
# s = "qvnnnnnuuuuuuutttttttt"
# print(oneSwap(s))
# [Efficient Approach] Using Frequency Array - O(n) time and O(1) space

# Function to count distinct strings after one swap
def countStrings(s):
    n = len(s)

    # Array to count character frequencies
    map = [0] * 26
    ans = 0

    # Count valid swaps, avoiding duplicates
    for i in range(n):
        ans += (i - map[ord(s[i]) - ord('a')])
        map[ord(s[i]) - ord('a')] += 1

    # Check for any duplicate character
    for i in range(26):
        if map[i] > 1:
            ans += 1
            break

    return ans


if __name__ == "__main__":
    s = "qvnnnnnuuuuuuutttttttt"
    # Output the count of distinct strings after one swap
    print(countStrings(s))
