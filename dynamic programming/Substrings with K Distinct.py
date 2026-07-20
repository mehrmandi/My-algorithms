# def count_substrings_with_at_most_k_distinct_chars(s, k):
#     left, right, n, distinct_count, substring_count = 0, 0, len(s), 0, 0
#
#     char_frequency = [0] * 26
#
#     while right < n:
#         char_index = ord(s[right]) - ord('a')
#         char_frequency[char_index] += 1
#
#         if char_frequency[char_index] == 1:
#             distinct_count += 1
#
#         while distinct_count > k:
#             char_frequency[ord(s[left]) - ord('a')] -= 1
#
#             if char_frequency[ord(s[left]) - ord('a')] == 0:
#                 distinct_count -= 1
#
#             left += 1
#
#         substring_count += (right - left + 1)
#
#         right += 1
#
#     return substring_count
#
#
# def count_substrings_with_exactly_k_distinct_chars(s, k):
#     count_at_most_k = count_substrings_with_at_most_k_distinct_chars(s, k)
#     print(count_at_most_k)
#
#     count_at_most_k_minus_1 = count_substrings_with_at_most_k_distinct_chars(
#         s, k - 1)
#     print(count_at_most_k_minus_1)
#
#     return count_at_most_k - count_at_most_k_minus_1

#
# def main():
#     input_string = "aacfssa"
#     k = 3
#     result = count_substrings_with_exactly_k_distinct_chars(input_string, k)
#
#     print("The number of substrings with exactly",
#           k, "distinct characters is:", result)
#
#
# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------------------
def countkDist(s, k):
    n = len(s)
    res = 0

    # Consider all substrings beginning with str[i]
    for i in range(n):
        dist_count = 0
        cnt = [0] * 26  # To store count of characters from 'a' to 'z'

        # Consider all substrings between str[i..j]
        for j in range(i, n):
            # If this is a new character for this substring, increment dist_count.
            if cnt[ord(s[j]) - ord('a')] == 0:
                dist_count += 1

            # Increment count of current character
            cnt[ord(s[j]) - ord('a')] += 1

            # If distinct character count becomes k, then increment result.
            if dist_count == k:
                res += 1
            if dist_count > k:
                break

    return res