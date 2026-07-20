class TreeNode:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v


def buildTree(preorder, inorder):
    res = []
    if not preorder or not inorder:
        return None

    inorder_map = {val: index for index, val in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end, res):
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        in_index = inorder_map[root_val]

        left_size = in_index - in_start

        root.left = build(pre_start + 1, pre_start + left_size, in_start, in_index - 1, res)

        root.right = build(pre_start + left_size + 1, pre_end, in_index + 1, in_end, res)

        res.append(root.data)
        return res

    return build(0, len(preorder) - 1, 0, len(inorder) - 1, res)




inorder = [3, 1, 4, 0, 2, 5]
preorder = [0, 1, 3, 4, 2, 5]

print(buildTree(preorder, inorder))
