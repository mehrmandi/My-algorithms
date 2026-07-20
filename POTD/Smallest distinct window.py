def find_smallest_window(s):
    unique_chars = set(s)  # Set of unique characters
    required_count = len(unique_chars)

    char_count = {}
    left = 0
    min_length = float('inf')
    min_window = ""

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) == required_count:
            window_size = right - left + 1
            if window_size < min_length:
                min_length = window_size
                min_window = s[left:right+1]

            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

    return min_length, min_window



    
    
str = "geeksforgks"
print(find_smallest_window(str))
