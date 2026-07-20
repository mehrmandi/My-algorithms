# [Expected Approach] By storing sum on the longer list - O(m + n) Time and O(1) Space-------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev

def addTwoLists(head1, head2):
    if not head1:
        return head2
    
    if not head2:
        return head1
    
    head1 = reverseList(head1)
    head2 = reverseList(head2)
    
    sumList = None
    carry = 0

    # Loop until both lists and carry are exhausted
    while head1 is not None or head2 is not None or carry > 0:
        newVal = carry

        if head1 is not None:
            newVal += head1.data
            head1 = head1.next
        if head2 is not None:
            newVal += head2.data
            head2 = head2.next

        carry = newVal // 10
        newVal = newVal % 10

        # Create a new node and link it at the front
        newNode = Node(newVal)
        newNode.next = sumList
        sumList = newNode

    # Return the final sum list
    return sumList
    
        
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
# head1.next.next.next = Node(1)
# head1.next.next.next.next = Node(0)

head2 = Node(9)
head2.next = Node(9)
head2.next.next = Node(9)
# head2.next.next.next = Node(1)
# head2.next.next.next.next = Node(0)

print(addTwoLists(head1, head2))
