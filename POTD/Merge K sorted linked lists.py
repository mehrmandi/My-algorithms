# Time Complexity: O(n * k * log k), where n is the number of nodes in the longest list.
# Auxiliary Space: O(log k), used for recursion.



class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def mergeTwo(head1, head2):
    dummy = Node(-1)
    curr = dummy

    while head1 is not None and head2 is not None:

        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next


    if head1 is not None:
        curr.next = head1
    else:
        curr.next = head2

    return dummy.next


def mergeListsRecur(i, j, arr):
    print(i, j, arr[i].data, arr[j].data)
    if i == j:
        return arr[i]

    mid = i + (j - i) // 2

    head1 = mergeListsRecur(i, mid, arr)

    head2 = mergeListsRecur(mid + 1, j, arr)

    head = mergeTwo(head1, head2)

    return head


def mergeKLists(arr):
    if len(arr) == 0:
        return None

    return mergeListsRecur(0, len(arr) - 1, arr)


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next


k = 3

arr = [None] * k

arr[0] = Node(1)
arr[0].next = Node(3)
arr[0].next.next = Node(5)
arr[0].next.next.next = Node(7)

arr[1] = Node(2)
arr[1].next = Node(4)
arr[1].next.next = Node(6)
arr[1].next.next.next = Node(8)

arr[2] = Node(0)
arr[2].next = Node(9)
arr[2].next.next = Node(10)
arr[2].next.next.next = Node(11)

head = mergeKLists(arr)

printList(head)
