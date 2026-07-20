from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def levelOrder(root):
    res = []
    if not root:
        return res

    queue = deque([root])
    reverse = True

    while queue:
        n = len(queue)
        
        for i in range(n):
            if reverse:
                curr = queue.pop()
                res.append(curr.data)

                if curr.right:
                    queue.appendleft(curr.right)
                if curr.left:
                    queue.appendleft(curr.left)
            else:
                curr = queue.popleft()
                res.append(curr.data)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        reverse = not reverse
        
    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)



print(levelOrder(root))
