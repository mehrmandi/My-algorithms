# Given root of a binary tree in which all node values are distinct, count pairs of nodes that violate any of the following Binary Search Tree(BST) properties.


# All values in the left subtree are strictly smaller.
# All values in the right subtree are strictly greater.

# Count Inversions Using Merge Sort - O(n log n) Time and O(n) Space

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inorder(root, arr):
    if root is None:
        return

    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, countLeft = mergeSort(arr[:mid])
    right, countRight = mergeSort(arr[mid:])

    merged = []
    i = j = 0
    count = countLeft + countRight

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # Count inversions formed with the remaining left elements.
            count += len(left) - i
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count


def pairsViolatingBST(root):
    arr = []
    inorder(root, arr)

    _, count = mergeSort(arr)
    return count


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(50)
    root.right = Node(40)

    root.right.left = Node(20)
    root.right.right = Node(30)

    print(pairsViolatingBST(root))
