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


def isPalindrome(head):
    if not head or not head.next:
        return True
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    second_half = reverseList(slow) 
    
    first = head
    second = second_half

    while second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next

    return True
    
           
        
        
            

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(3)
head1.next.next.next.next = Node(2)
head1.next.next.next.next.next = Node(1)

print(isPalindrome(head1))