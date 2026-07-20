class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def insertLevelOrder(arr):
    if not arr:
        return None

    n = len(arr)
    nodes = [None if val is None else Node(val) for val in arr]

    for i in range(n):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < n and nodes[left_index] is not None:
                nodes[i].left = nodes[left_index]
            if right_index < n and nodes[right_index] is not None:
                nodes[i].right = nodes[right_index]

    return nodes[0]


def postorder(root, max_val):
    if root is None:
        return 0

    left = max(postorder(root.left, max_val), 0)
    right = max(postorder(root.right, max_val), 0)
    max_val = max(max_val, left + right + root.data)
    return max(left, right) + root.data



def finalMaxSum(arr):
    max_val = 0
    root = insertLevelOrder(arr)
    postorder(root, max_val)
    return max_val


arr = [10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4]
print(finalMaxSum(arr))

