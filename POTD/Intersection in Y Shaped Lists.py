# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def intersectPoint(head1, head2):
#     count1 = 0
#     count2 = 0
    
#     curr1 = head1
#     while curr1:
#         count1 += 1
#         curr1 = curr1.next
        
#     curr2 = head2
#     while curr2:
#         count2 += 1
#         curr2 = curr2.next
        
#     pivot = min(count1, count2)
    
#     while count1 > pivot:
#         head1 = head1.next
#         count1 -= 1
        
#     while count2 > pivot:
#         head2 = head2.next
#         count2 -= 1
        
    
#     while head1 and head2:
#         if head1 == head2:
#             return head1.data
#         head1 = head1.next
#         head2 = head2.next
    

# head = Node(15)
# head.next = Node(30)
# head.next.next = Node(40)

# head1 = Node(4)
# head1.next = head

# head2 = Node(3)
# head2.next = Node(6)
# head2.next.next = Node(9)
# head2.next.next.next = head

# print(intersectPoint(head1, head2))



# [Expected Approach - 3] Intersection Detection using List Reversal and Floyd’s Cycle-Finding Algorithm--------------


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# reverses a linked list


def reverse(node):
    prev = None
    curr = node
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# finds the intersection point of two
# linked lists


def intersectPoint(head1, head2):
    if not head1 or not head2:
        return None

    # reverse the second list
    revHead2 = reverse(head2)

    # attach reversed second list to the
    # end of the first
    temp = head1
    while temp.next:
        temp = temp.next
    temp.next = revHead2

    # detect cycle using Floyd’s algorithm
    slow = head1
    fast = head1

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head1
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


if __name__ == "__main__":
    # first list: 10 -> 15 -> 30
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    # second list: 3 -> 6 -> 9 -> 15 -> 30
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)

    # intersection at node with value 15
    head2.next.next.next = head1.next

    interPt = intersectPoint(head1, head2)

    if interPt is None:
        print("-1")
    else:
        print(interPt.data)
