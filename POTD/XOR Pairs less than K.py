class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.count = 0


class XORTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]
            node.count += 1

    def count_less_than_k(self, num, k):
        node = self.root
        ans = 0

        for i in range(31, -1, -1):
            if not node:
                break

            bit_num = (num >> i) & 1
            bit_k = (k >> i) & 1

            if bit_k == 1:
                # Add all numbers matching XOR bit = 0
                if node.child[bit_num]:
                    ans += node.child[bit_num].count

                # Move to XOR bit = 1 branch
                node = node.child[1 - bit_num]

            else:
                # Must match XOR bit = 0
                node = node.child[bit_num]

        return ans


def count_pairs(arr, k):
    trie = XORTrie()
    result = 0

    for x in arr:
        result += trie.count_less_than_k(x, k)
        trie.insert(x)

    return result



# Example
arr = [1, 2, 3, 5]
k = 5
print(count_pairs(arr, k))  # Output: 4
