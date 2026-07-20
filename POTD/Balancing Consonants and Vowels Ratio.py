# # from collections import defaultdict

# # # Time Complexity: O(n * l), where n is the number of strings and l is the average length of each string, since each character in all strings is processed once.
# # Space Complexity: O(n), due to the prefix sum frequency map which can store up to n unique prefix values.
# def countBalanced(arr):
#     n = len(arr)
#     vowels = ["a", "e", "i", "o", "u"]
#     new_arr = [0 for _ in range(n)]
    
#     for i in range(n):
#         val = 0
#         for j in arr[i]:
#             if j in vowels:
#                 val += 1
#             else:
#                 val -= 1
#         new_arr[i] = val
        
#     res = 0
#     hash = {0: 1}
#     prefix = 0

#     for i in range(n):
#         prefix += new_arr[i]
#         res += hash.get(prefix, 0)
#         hash[prefix] = hash.get(prefix, 0) + 1

#     return res


# arr = ["aeio", "aa", "bc", "ot", "cdbd"]
# print(countBalanced(arr))


# Time Complexity: O(n * l), where n is the number of strings and l is the average length of each string, since each character in all strings is processed once.
# Space Complexity: O(n), due to the prefix sum frequency map which can store up to n unique prefix values.

# Function to check if a character is a vowel

# def isVowel(ch):
#     return ch in 'aeiou'

# # Function to count the number of balanced subarrays


# def countBalanced(arr):
#     n = len(arr)
#     res = 0
#     prefix = 0

#     # Map to store frequency of prefix sums
#     freq = defaultdict(int)

#     # Initial prefix sum is 0 (empty prefix is considered balanced)
#     freq[0] = 1

#     # Traverse the array of strings
#     for i in range(n):
#         score = 0

#         # Calculate net score of current
#         # string: +1 for vowel, -1 for consonant
#         for ch in arr[i]:
#             if isVowel(ch):
#                 score += 1
#             else:
#                 score -= 1

#         # Update the running prefix sum
#         prefix += score

#         # If this prefix sum has been seen before,
#         # then the subarray between previous and
#         # current prefix is balanced
#         res += freq[prefix]

#         # Increment the frequency of this prefix sum
#         freq[prefix] += 1

#     return res


# if __name__ == "__main__":
#     arr = ["aeio", "aa", "bc", "ot", "cdbd"]
#     print(countBalanced(arr))



