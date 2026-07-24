# Single DFS with Parent Tracking - O(n) Time and O(n) Space

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# DFS traversal while maintaining current consecutive length


def dfs(currentNode, parentNode, currentLength, longestPath):
    if currentNode is None:
        return

    # Check whether consecutive sequence continues
    if parentNode and currentNode.data == parentNode.data + 1:
        currentLength += 1
    else:
        currentLength = 1

    # Update the best answer found so far
    longestPath[0] = max(longestPath[0], currentLength)

    dfs(currentNode.left, currentNode, currentLength, longestPath)
    dfs(currentNode.right, currentNode, currentLength, longestPath)


def longestConsecutive(root):
    if root is None:
        return -1

    longestPath = [0]

    dfs(root, None, 0, longestPath)

    return -1 if longestPath[0] == 1 else longestPath[0]


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(3)

    print(longestConsecutive(root))
