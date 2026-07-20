class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def reverse_k_group(head, k):
    if head is None:
        return head

    curr = head
    newHead = None
    tail = None

    while curr is not None:
        groupHead = curr
        prev = None
        nextNode = None
        count = 0

        # Reverse the nodes in the current group
        while curr is not None and count < k:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            count += 1

        # If newHead is null, set it to the
        # last node of the first group
        if newHead is None:
            newHead = prev

        # Connect the previous group to the
        # current reversed group
        if tail is not None:
            tail.next = prev

        # Move tail to the end of
        # the reversed group
        tail = groupHead

    return newHead


def printList(head):
    while head:
        print(head.data, end="")
        if head.next:
            print(" -> ", end="")
        head = head.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

k = 2

head = reverse_k_group(head, k)

printList(head)
