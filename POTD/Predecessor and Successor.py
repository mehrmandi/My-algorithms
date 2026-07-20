class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_predecessor_successor(root, key):
    



# Example BST
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(17)
root.right.right = Node(25)

key = 15
predecessor, successor = find_predecessor_successor(root, key)
print(f"Predecessor of {key}: {predecessor}")
print(f"Successor of {key}: {successor}")


# [Expected Approach] Using BST Search - O(h) Time and O(1) Space
            
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None

# # Function to find maximum in left subtree (Predecessor)


# def rightMost(node):
#     while node.right is not None:
#         node = node.right
#     return node

# # Function to find minimum in right subtree (Successor)


# def leftMost(node):
#     while node.left is not None:
#         node = node.left
#     return node

# # Function to find predecessor and successor


# def findPreSuc(root, key):
#     pre = None
#     suc = None
#     curr = root

#     while curr is not None:
#         if curr.data < key:
#             pre = curr
#             curr = curr.right
#         elif curr.data > key:
#             suc = curr
#             curr = curr.left
#         else:
#             # If key is found
#             if curr.left is not None:
#                 pre = rightMost(curr.left)
#             if curr.right is not None:
#                 suc = leftMost(curr.right)
#             break

#     return [pre, suc]  # return as a list


# # Main execution
# if __name__ == "__main__":
#     key = 65

#     # Construct the BST
#     root = Node(50)
#     root.left = Node(30)
#     root.right = Node(70)
#     root.left.left = Node(20)
#     root.left.right = Node(40)
#     root.right.left = Node(60)
#     root.right.right = Node(80)

#     result = findPreSuc(root, key)
#     pre, suc = result[0], result[1]

#     if pre is not None:
#         print(pre.data, end=" ")
#     else:
#         print(-1, end=" ")

#     if suc is not None:
#         print(suc.data)
#     else:
#         print(-1)
