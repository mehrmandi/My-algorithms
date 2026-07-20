class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def constructTreeUtil(pre, post, preIndex, l, h, postMap):
    print(preIndex, l, h)
    if preIndex[0] >= len(pre) or l > h:
        print("111111111111111")
        return None

    root = Node(pre[preIndex[0]])
    preIndex[0] += 1
    print("root, preindex", root.data, preIndex)

    # If there is only one element,
    # return it as leaf node
    if l == h:
        print("222222222")
        return root

    # Find the next preorder element
    # in postorder using hashmap
    i = postMap[pre[preIndex[0]]]
    if i <= h:
        root.left = constructTreeUtil(pre, post, preIndex,
                                      l, i, postMap)
        print("left", root.data, root.left.data)
        root.right = constructTreeUtil(pre, post, preIndex,
                                       i + 1, h - 1, postMap)
        print("right", root.data, root.right.data)

    return root
    

def constructTree(pre, post):
    postMap = {val: idx for idx, val in enumerate(post)}
    preIndex = [0]
    return constructTreeUtil(pre, post, preIndex,
                             0, len(pre) - 1, postMap)
    
    
    
    
    
    
pre = [20, 8, 5, 2, 1, 3, 10, 14, 22, 4, 25, 28]
post = [2, 1, 5, 10, 14, 3, 8, 4, 28, 25, 22, 20]
print(constructTree(pre, post))


# [20, 8, 5, 3, 10, 14, 22, 4, 25, 28]
# [5, 10, 14, 3, 8, 4, 28, 25, 22, 20]
#  Create binary tree
#       20
#       /  \
#     8     22
#    / \    / \
#   5   3  4   25
#  / \  / \    /
# 2   1 10 14  28
