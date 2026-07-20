# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None


# def inOrderTraversal(root, res):
#     if not root:
#         return
#     inOrderTraversal(root.left, res)
#     res.append(root.data)
#     inOrderTraversal(root.right, res)
    

# def printKClosest(arr, k, x):
#     print(arr)

#     # Sort based on distance from x, break ties by preferring smaller number
#     sorted_by_closeness = sorted(arr, key=lambda num: (abs(num - x), num))
#     print(sorted_by_closeness)

#     # Take the first k elements
#     result = sorted_by_closeness[:k]

#     return result
    
# def getKClosest(root, target, k):
#     res = []
    
#     inOrderTraversal(root, res)
    
#     return printKClosest(res, k, target)
    
    


# root = Node(5)
# root.left = Node(4)
# root.right = Node(8)
# root.left.left = Node(1)
# # root.left.right = Node(12)
# # root.left.right.left = Node(10)
# # root.left.right.right = Node(14)
# target = 5
# k = 2

# print(getKClosest(root, target, k))
# Time Complexity: O(n)----------------------------------------
# Auxiliary Space: O(h+k), h = height of BST---------------------------------

from collections import deque

# Node structure


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Performs inorder traversal to collect k nodes
# closest to a given target value in a BST


def getInorder(node, x, k, kClosest):
    if node is None:
        return

    getInorder(node.left, x, k, kClosest)

    # if size < k, include node
    if len(kClosest) < k:
        kClosest.append(node.data)

    # else check if current node is
    # closer to target
    elif abs(kClosest[0] - x) > abs(node.data - x):
        kClosest.popleft()
        kClosest.append(node.data)
    else:
        return

    getInorder(node.right, x, k, kClosest)

# Function to find k values in BST closest to the target


def getKClosest(root, target, k):
    dq = deque()
    getInorder(root, target, k, dq)

    # convert deque to list
    ans = []
    while dq:
        ans.append(dq.popleft())

    return ans


if __name__ == "__main__":

    # Create BST:
    #            20
    #           /  \
    #          8    22
    #        /   \
    #       4    12
    #           /   \
    #         10    14

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    k = 3
    target = 17
    result = getKClosest(root, target, k)

    for val in result:
        print(val, end=" ")
    print()
