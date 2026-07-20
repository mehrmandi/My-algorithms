# [Expected Approach] Using In-Order traversal - O(k) Time and O(h) Space----------------------------------------

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None


# def kthSmallest(root, k):
#        # code here.
#         def kthSmallestRecur(root, cnt, k):
#             if root is None:
#                 return -1
            

#             left = kthSmallestRecur(root.left, cnt, k)

#             if left != -1:
#                 return left

#             cnt[0] += 1

#             if cnt[0] == k:
#                 return root.data

#             right = kthSmallestRecur(root.right, cnt, k)
#             return right

#         cnt = [0]
#         return kthSmallestRecur(root, cnt, k)


# k = 5
# root = Node(20)
# root.left = Node(8)
# root.right = Node(22)
# root.left.left = Node(4)
# # root.left.left.left = Node(3)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)

# print(kthSmallest(root, k))


# [Expected Approach] Using Morris Inorder Traversal - O(n) Time and O(1) Space-----------------------------


# Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to find kth Smallest


def kthSmallest(root, k):
    count = 0
    curr = root

    while curr is not None:
        if curr.left is None:
            print("left None")
            count += 1
            if count == k:
                return curr.data
            curr = curr.right
            print("curr", curr.data)
        else:
            # Find the inorder predecessor of curr
            prev = curr.left
            print("prev", prev.data)
            while prev.right is not None and prev.right != curr:
                prev = prev.right
                print("prev right", prev.data)

            # Make curr the right child of its inorder predecessor
            if prev.right is None:
                prev.right = curr
                curr = curr.left
                print("right None", curr.data)
            else:
                print("final else", curr.data)
                count += 1
                if count == k:
                    return curr.data

                # Revert the changes made in the tree structure
                prev.right = None
                curr = curr.right
                print("print", prev.data, curr.data)
    return -1


if __name__ == "__main__":
    # Binary search tree
    #      20
    #    /   \
    #   8     22
    #  / \
    # 4   12
    #    /  \
    #   10   14
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    k = 3

    print(kthSmallest(root, k))
