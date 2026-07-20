# [Expected Approach - 2] By Updating Links of Nodes - O(n) Time and O(1) Space:--------------------------------


# Python Program to sort a linked list 0s, 1s
# or 2s by updating links

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Sort a linked list of 0s, 1s and 2s
# by changing pointers


def sortList(head):
    if not head or not head.next:
        return head

    # Create three dummy nodes to point to beginning of
    # three linked lists. These dummy nodes are created to
    # avoid null checks.
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)

    # Initialize current pointers for three
    # lists
    zero = zeroD
    one = oneD
    two = twoD

    # Traverse list
    curr = head
    while curr:
        if curr.data == 0:

            # If the data of current node is 0,
            # append it to pointer zero and update zero
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:

            # If the data of cu
            # append it to pointer one and update one
            one.next = curr
            one = one.next
        else:
            # If the data of current node is 2,
            # append it to pointer two and update two
            two.next = curr
            two = two.next
        curr = curr.next

    # Combine the three lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None

    # Updated head
    head = zeroD.next

    return head


def printList(node):
    while node is not None:
        print(node.data, end=' ')
        node = node.next
    print()


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 1 -> 2 -> 1 -> 0 -> NULL
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)

    print("Linked List before Sorting: ", end='')
    printList(head)

    head = sortList(head)

    print("Linked List after Sorting: ", end='')
    printList(head)
