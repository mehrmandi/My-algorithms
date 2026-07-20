class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        # self.lCount = l

# def collectLeftBoundry(root, path, counter, k):
#     if not root:
#         return
#     print("left", root.data, path, counter[0], k)
#     if root.left:
#         path.append(root.left.data)
#         counter[0] += 1
#         collectLeftBoundry(root.left, path, counter, k)
#
#     if counter[0] >= k:
#         print(counter[0], k)
#         return counter[0]
#
#
#
#
# def rootMake(root, path, counter, k, res):
#     if not root:
#         return
#
#     print("rootmaker", root.data, path, counter[0], k)
#
#     if root.left:
#         if collectLeftBoundry(root, path, counter, k):
#             print("shod", path, k)
#             res[0] = path[-k]
#             return
#         else:
#             k -= counter[0]
#             if root.left.right:
#                 print("root.left.right")
#                 path.append(root.left.right.data)
#                 counter[0] += 1
#                 rootMake(root.left.right, path, counter, k, res)
#
#             else:
#                 path.append(root.right.data)
#                 counter[0] += 1
#                 rootMake(root.right, path, counter, k, res)
#
#


# def kthSmallest(root, k):
#     path = []
#     counter = [0]
#     res = [0]
#     rootMake(root, path, counter, k, res)
#     return res[0]
#
#

# def kthSmallestRecur(root, k):
#     if root is None:
#         return -1
#
#     # Search left subtree
#     if k[0] < root.lCount + 1:
#         return kthSmallestRecur(root.left, k)
#
#     # return curr node
#     elif k[0] == root.lCount + 1:
#         return root.data
#
#     # decrement k by (lCount+1) and
#     # search right subtree
#     else:
#         k[0] -= (root.lCount + 1)
#         return kthSmallestRecur(root.right, k)
#
#
# # Function to find kth smallest value in BST.
# def kthSmallest(root, k):
#     kRef = [k]
#     return kthSmallestRecur(root, kRef)
#

# def kthSmallestRecur(root, cnt, k):
#     if root is None:
#         return -1
#
#     # Process left subtree.
#     left = kthSmallestRecur(root.left, cnt, k)
#
#     # If kth smallest is found in left
#     # subtree, then return it.
#     if left != -1:
#         return left
#
#     # increment node count
#     cnt[0] += 1
#
#     # If curr node is kth smallest,
#     # return it.
#     if cnt[0] == k:
#         return root.data
#
#     # Else process the right subtree
#     # and return its value.
#     right = kthSmallestRecur(root.right, cnt, k)
#     return right
#
#
# # Function to find kth smallest value in BST.
# def kthSmallest(root, k):
#     cnt = [0]
#     return kthSmallestRecur(root, cnt, k)


def doit(root, ans):
    if root == None:
        return
    else:
        doit(root.left, ans)
        ans.append(root.data)
        doit(root.right, ans)


def kthSmallest(root, k):
    ans = []
    doit(root, ans)
    if len(ans) < k:
        return (-1)
    return (ans[k - 1])


k = 5
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.left.left = Node(3)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(kthSmallest(root, k))
