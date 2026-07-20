from collections import deque
# [Expected Approach - 2] - Using Deque - O(n) Time and O(n) Space-----------------------------
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def zigZagTraversal(root):
    res = []
    q = deque([(root, 1)])
    
    while q:
        n = len(q)
        level_order = []
        level = 0
        for i in range(n):
            node, level = q.pop()
            level_order.append(node.data)
            
            if node.left:
                q.appendleft((node.left, level + 1))
                
            if node.right:
                q.appendleft((node.right, level + 1))
        
        if level % 2 == 0:
            level_order.reverse()
            
        res.extend(level_order)
        
    return res
                

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
root.left.left.right = Node(1)
root.left.left.left = Node(2)

    #       20
    #       /  \
    #     8     22
    #    / \    / \
    #   5   3  4   25
    #  / \  / \    /
    # 2   1 10 14  28


print(zigZagTraversal(root))