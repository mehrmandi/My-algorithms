# Given a lowercase string s and a dictionary d[] containing lowercase words, find the longest word in the dictionary that can be obtained by deleting some characters from s without changing the order of the remaining characters.

# Note: If multiple words have the same maximum length, return the lexicographically smallest one. If no valid word exists, return an empty string.

# Index Mapping + Binary Search - O( | s | + n * maxWordLen * log | s|) Time O(|s|) Space

from bisect import bisect_right


# Returns True if 'word' is a subsequence of string 's'
def isSubsequence(word, pos):

    prevIndex = -1

    for ch in word:

        # All positions where character 'ch' occurs in s
        indices = pos[ord(ch) - ord('a')]

        # Find first occurrence of ch after prevIndex
        idx = bisect_right(indices, prevIndex)

        # No valid next position found
        if idx == len(indices):
            return False

        # Update previously matched index
        prevIndex = indices[idx]

    return True

def findLongestWord(s: str, d: list) -> str:
    pos = [[] for _ in range(26)]

    for i in range(len(s)):
        pos[ord(s[i]) - ord('a')].append(i)

    res = ""

    for word in d:

        # Skip smaller words directly
        if len(word) < len(res):
            continue

        # Check whether word is subsequence of s
        if isSubsequence(word, pos):

            # Prefer longer word
            # If same length, prefer lexicographically smaller word
            if (len(word) > len(res) or
                    (len(word) == len(res) and word < res)):

                res = word

    return res


            

d = ['abc', 'zvhxunzidu', 'lwmuhvrx', 'ummqs', 'ldwkflyojk', 'utcwugo', 'cbdij', 'gqdo','rstgcd', 'nax', 'yrmngyl', 'momktfk', 'kvwpxiodo', 'boh', 'msxwhb', 'i', 'etivsvfdxy', 'aw']
s = "jhvsrcgabkdhcviunziotyzychypzpkrofv"

print(findLongestWord(s, d))