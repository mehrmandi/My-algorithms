def stringStack(pat, tar):
    i = len(pat) - 1
    j = len(tar) - 1

    while i >= 0 and j >= 0:

        # If characters don’t match, simulate a deletion
        # by skipping previous character in 'pat'
        if pat[i] != tar[j]:
            i -= 2

        # If characters match, move both
        # pointers to the previous character
        else:
            i -= 1
            j -= 1

    # If we have successfully matched all
    # characters of 'tar', return true
    return j < 0

pat = "dicxdcuba"
tar = "dia"
print(stringStack(pat, tar))
