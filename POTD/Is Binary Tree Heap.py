class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(arr):
    n = len(arr)
    root = Node(arr[0])
    i = 1
    q = [root]
    
    while i < n:
        curr = q.pop(0)
        if curr:
            left_val = arr[i]
            curr.left = Node(left_val) if left_val else None
            q.append(curr.left)
            i += 1
            
            if i < n:
                right_val = arr[i]
                curr.right = Node(right_val) if right_val else None
                q.append(curr.right)
                i += 1
                      
    return root

def isComplete(root):
    if not root:
        return True
    
    q = [root]
    null_node = False
    
    while q:
        curr = q.pop(0)
        if curr:
            if null_node:
                return False
            q.append(curr.left)
            q.append(curr.right)
        else:
            null_node = True
    
    return True

def isMaxHeap(root):
    if not root:
        return True
    
    left = root.left
    right = root.right
    
    if (left and root.data < left.data) or (right and root.data < right.data):
        return False
    
    return isMaxHeap(left) and isMaxHeap(right)


def isHeap(arr):
    root = buildTree(arr)
    return isComplete(root) and isMaxHeap(root) 

# arr = [97, 46, 37, 12, 3, 7, 31, 6, 9]
arr = [97, 46, 37, 12, 3, 7, 31, None, 2, 4]
print(isHeap(arr))


# [Approach 3] Using Level Order Traversal – O(n) Time and O(n) Space


# class Node:
#     def __init__(self, k):
#         self.data = k
#         self.left = None
#         self.right = None


# def isHeap(root):
#     queue = [root]
#     flag = False
#     while queue:
#         temp = queue.pop(0)
#         if temp.left:
#             if flag or temp.left.data > temp.data:
#                 return False
#             queue.append(temp.left)
#         else:
#             flag = True
#         if temp.right:
#             if flag or temp.right.data > temp.data:
#                 return False
#             queue.append(temp.right)
#         else:
#             flag = True
#     return True


# if __name__ == "__main__":

#     # Binary Tree Representation
#     #        10
#     #      /    \
#     #     9      8
#     #    / \    / \
#     #   7   6  5   4

#     root = Node(10)
#     root.left = Node(9)
#     root.right = Node(8)
#     root.left.left = Node(7)
#     root.left.right = Node(6)
#     root.right.left = Node(5)
#     root.right.right = Node(4)

#     print(isHeap(root))
