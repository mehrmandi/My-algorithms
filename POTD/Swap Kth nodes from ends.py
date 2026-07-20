
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def swapKth(head, k):
    n = 0
    
    curr = head
    
    while curr:
        curr = curr.next
        n += 1
        
    if k > n:
        return head
    
    if 2 * k - 1 == n:
        return head


    prev1 = None
    node1 = head
    
    for _ in range(1, k):
        prev1 = node1
        node1 = node1.next
        
    prev2 = None
    node2 = head
    for _ in range(1, n - k):
        prev2 = node2
        node2 = node2.next
        
    if prev1:
        prev1.next = node2
    else:
        head = node2

    if prev2:
        prev2.next = node1
    else:
        head = node1

    node1.next, node2.next = node2.next, node1.next

    return head

        
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 1

print(swapKth(head, k))
    
    

