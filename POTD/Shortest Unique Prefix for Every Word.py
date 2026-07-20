
# Trie with Frequency Tracking - O(n × L) Time and O(n × L) Space
class Node:
    def __init__(self):
        self.freq = 0
        self.children = [None] * 26

    # Insert a word into the Trie
    def insert(self, word):
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = Node()
            curr = curr.children[ord(c) - ord('a')]
            curr.freq += 1

    # Find the ending index of minimum
    # unique prefix for given word
    def findPrefix(self, word):
        curr = self
        for i in range(len(word)):
            curr = curr.children[ord(word[i]) - ord('a')]

            # If frequency is 1, we found the unique prefix
            if curr.freq == 1:
                return i
        return len(word) - 1
    

def findPrefixes(arr):
    n = len(arr)

    # Create root node of Trie
    root = Node()

    # Insert all words into the Trie
    for i in range(n):
        root.insert(arr[i])

    # List to store result prefixes
    result = []

    # Find minimum unique prefix for each word
    for i in range(n):
        word = arr[i]

        # Get ending index of minimum prefix
        endIndex = root.findPrefix(word)

        # Add substring from start to endIndex to result
        result.append(word[:endIndex + 1])

    return result

        
    


arr = ["zebra", "dog", "duck", "dove"]
print(findPrefixes(arr))
    