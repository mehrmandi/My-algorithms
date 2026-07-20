# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         cur = self.root
#         for ch in word:
#             if ch not in cur.children:
#                 cur.children[ch] = TrieNode()
#             cur = cur.children[ch]
#         cur.is_end = True

#     def dfs(self, node, path, result):
#         if not node.is_end:
#             return

#         # Update result if path is longer or lexicographically smaller at same length
#         if len(path) > len(result[0]) or (len(path) == len(result[0]) and path < result[0]):
#             result[0] = path

#         for ch in sorted(node.children.keys()):
#             self.dfs(node.children[ch], path + ch, result)


# def longest_valid_word(words):
#     trie = Trie()
#     for word in words:
#         trie.insert(word)

#     result = [""]
#     for ch in sorted(trie.root.children.keys()):
#         trie.dfs(trie.root.children[ch], ch, result)

#     return result[0]
    
    
# words = ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
# print(longestString(words))


# trie node definition

# Time Complexity: O(n*k), one pass for insertion and one for prefix checks where n is the number of words and k is the average word length,
# Auxiliary Space: O(n*k), where n is the number of words and k is the average word length.




class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert a word into the trie
    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        # marking the end of the word
        node.isEnd = True

    # check if all prefixes of the word exist in the trie
    def allPrefixesExist(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            node = node.children[idx]

            # if the prefix is missing or not marked as end
            if not node or not node.isEnd:
                return False
        return True


# Function to find the longest word whose
# all prefixes exist in the list
def longestString(words):
    trie = Trie()

    # insert all words into the trie
    for word in arr:
        trie.insert(word)

    result = ""

    # check each word
    for word in arr:

        # if all prefixes exist
        if trie.allPrefixesExist(word):

            # update result if word is longer or
            # lexicographically smaller
            if len(word) > len(result) or (len(word) == len(result)
                                           and word < result):
                result = word

    return result


if __name__ == "__main__":
    arr = ["ab", "a", "abc", "abd"]
    print(longestString(arr))

