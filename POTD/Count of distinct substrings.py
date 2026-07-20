class TrieNode:
    def __init__(self):
        self.children = {}


def countSubs(s):
    root = TrieNode()
    n = len(s)
    count = 0
    
    for i in range(n):
        node = root
        for ch in s[i:]:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                count += 1
            node = node.children[ch]
            
    return count
    
    
s = "ababa"
print(countSubs(s))