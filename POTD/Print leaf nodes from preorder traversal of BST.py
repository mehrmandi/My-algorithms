def find_leaf_nodes(preorder):
    result = []          # To store the leaf nodes
    n = len(preorder)
    index = [0]          # Mutable index pointer for recursion

    def helper(min_val, max_val):
        # If index is out of bounds, no node exists
        if index[0] >= n:
            return None

        curr_val = preorder[index[0]]
        # If current value does not fit in the valid range, it doesn't belong here.
        if not (min_val < curr_val < max_val):
            return None

        # "Consume" the current node
        index[0] += 1

        # Process left subtree with an updated upper bound
        left_child = helper(min_val, curr_val)
        # Process right subtree with an updated lower bound
        right_child = helper(curr_val, max_val)

        # If neither child exists, then this node is a leaf node.
        if left_child is None and right_child is None:
            result.append(curr_val)

        # Return the current value for parent's reference (although the value itself isn't used further)
        return curr_val

    # Initialize recursion with the full range (using -infinity and infinity as boundaries)
    helper(float('-inf'), float('inf'))
    return result



# preorder = [4, 2, 1, 3, 6, 5, 7]

preorder = [40, 25, 10, 3, 17, 32, 30, 38, 78, 50, 64, 93]
print(find_leaf_nodes(preorder))
