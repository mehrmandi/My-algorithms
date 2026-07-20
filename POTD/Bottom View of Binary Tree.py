from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def bottomView(root):
    hash = {}
    res = []
    
    q = deque([(root, 0)])
    
    while q:
        n = len(q)
        
        for i in range(n):
            node, dis = q.pop()
            hash[dis] = node.data
            
            if node.left:
                q.appendleft((node.left, dis - 1))
            if node.right:
                q.appendleft((node.right, dis + 1))
                
    sorted_keys = sorted(hash)
    
    for key in sorted_keys:
        res.append(hash[key])
        
    return res
    


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right.left = Node(28)


print(bottomView(root))

# [Expected Approach - 1] Using DFS - O(n) Time and O(n) Space-----------------------------------------------------
# Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Pair class to store
# node data and its depth


class Pair:
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth


minHD = 0
maxHD = 0

# DFS function to fill hdMap with bottom-most nodes
# at each horizontal distance


def dfs(root, hd, depth, hdMap):
    global minHD, maxHD
    if root is None:
        return

    minHD = min(minHD, hd)
    maxHD = max(maxHD, hd)

    # If this horizontal distance is
    # being visited for the first time or
    # we're at a deeper level, update it
    if hd not in hdMap or depth >= hdMap[hd].depth:
        hdMap[hd] = Pair(root.data, depth)

    dfs(root.left, hd - 1, depth + 1, hdMap)
    dfs(root.right, hd + 1, depth + 1, hdMap)

# Returns the bottom view of a binary tree


def bottomView(root):
    if root is None:
        return []

    global minHD, maxHD
    minHD = 0
    maxHD = 0

    # Map to store the last node's data and its depth
    # at each horizontal distance (HD)
    hdMap = {}

    dfs(root, 0, 0, hdMap)

    result = []

    # Iterate through horizontal distances
    # in range from min HD to max HD
    for hd in range(minHD, maxHD + 1):
        result.append(hdMap[hd].data)

    return result


if __name__ == "__main__":

    # Create binary tree
    #       20
    #      /  \
    #    8     22
    #   / \     \
    #  5   3     25
    #     / \    /
    #    10 14  28

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right.right = Node(25)
    root.right.right.left = Node(28)

    minHD = 0
    maxHD = 0

    result = bottomView(root)

    print(*result)
    
    
# Node Structure
# [Expected Approach - 2] Using BFS - O(n) Time and O(n) Space------------------------------------
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def bottomView(root):

    if root is None:
        return []

    # HashMap to store
    # <vertical_index, node data>
    hash = {}

    minHD = 0
    maxHD = 0

    # Queue for level order traversal
    # with pair<Node, vertical index>
    q = deque()

    q.append([root, 0])

    while q:
        top = q.popleft()

        node = top[0]
        hd = top[1]

        # Update the horizontal distance -> node data
        hash[hd] = node.data

        minHD = min(minHD, hd)
        maxHD = max(maxHD, hd)

        if node.left is not None:
            q.append([node.left, hd - 1])

        if node.right is not None:
            q.append([node.right, hd + 1])

    ans = []
    for i in range(minHD, maxHD + 1):
        ans.append(hash[i])

    return ans


if __name__ == "__main__":
    #  Create binary tree
    #       20
    #       /  \
    #     8     22
    #    / \     \
    #   5   3     25
    #      / \    /
    #     10 14  28

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right.right = Node(25)
    root.right.right.left = Node(28)

    result = bottomView(root)
    print(*result)
