class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortedInsert(head, data):
    new_node = Node(data)

    # Case 1: If the list is empty
    if head is None:
        new_node.next = new_node  # Circular link
        return new_node

    # Case 2: If the new node should be the new head
    if data <= head.data:
        # Find the last node (which points to head)
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = new_node  # Last node points to new node
        new_node.next = head  # New node points to old head
        return new_node  # New head

    # Case 3: Insert somewhere in the middle
    curr = head
    while curr.next != head and curr.next.data < data:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node

    return head

# Example Usage


def printCircularList(head):
    temp = head
    if head is None:
        return
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print("HEAD")


# Creating a circular linked list: 1 -> 2 -> 4 -> HEAD
head = Node(1)
second = Node(2)
third = Node(4)

head.next = second
second.next = third
third.next = head  # Circular connection

# Insert new node with value 2
head = sortedInsert(head, 2)

# Print the list
printCircularList(head)
