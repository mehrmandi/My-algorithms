class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def reverse(head):
    
    prev_node = None
    curr = head
    while curr:
        curr.next, curr.prev = curr.prev, curr.next
        prev_node = curr
        curr = curr.prev
        
    return prev_node
        
    

head = Node(3)
head.next = Node(4)
head.prev = head
head.next.next = Node(5)
head.next.prev = head.next

print(reverse(head))
