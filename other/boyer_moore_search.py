def bad_character_table(pattern):
    """Creates the bad character shift table."""
    table = {}
    length = len(pattern)
    for i in range(length):
        table[pattern[i]] = i  # Last occurrence of character in pattern
    return table


def boyer_moore_search(text, pattern):
    """Searches for pattern in text using Boyer-Moore algorithm."""
    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or m > n:
        return []

    bad_char = bad_character_table(pattern)
    print(bad_char, n, m)
    matches = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        # Compare pattern from end to start
        while j >= 0 and pattern[j] == text[shift + j]:
            print("pattern[j], text[shift + j] ", j,
                  shift, pattern[j], text[shift + j])
            j -= 1

        if j < 0:
            matches.append(shift)
            # Shift pattern to align with next character in text
            shift += m - \
                bad_char.get(text[shift + m], -1) if shift + m < n else 1
        else:
            # Shift pattern based on bad character heuristic
            bad_char_index = bad_char.get(text[shift + j], -1)
            shift += max(1, j - bad_char_index)

    return matches


# Example usage
text = "AABAACAADAABAABA"
pattern = "AABA"
result = boyer_moore_search(text, pattern)
print("Pattern found at indices:", result)
