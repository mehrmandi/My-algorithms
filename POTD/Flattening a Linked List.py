# # Time Complexity: O(n * n * m) - where n is the no of nodes in the main linked list and m is the no of nodes in a single sub-linked list.
# # Auxiliary Space: O(n), the recursive functions will use a recursive stack of a size equivalent to a total number of nodes in the main linked list


# class Node:
#     def __init__(self, d):
#         self.data = d
#         self.next = None
#         self.bottom = None
        
        
# def merge(head1, head2):

#     # A dummy first node to store the result list
#     dummy = Node(-1)
#     tail = dummy

#     # Iterate till either head1 or head2 does not reach None
#     while head1 and head2:
#         if head1.data <= head2.data:

#             # Append head1 to the result
#             tail.bottom = head1
#             head1 = head1.bottom
#         else:

#             # Append head2 to the result
#             tail.bottom = head2
#             head2 = head2.bottom

#         # Move tail pointer to the next node
#         tail = tail.bottom

#     # Append the remaining nodes of the non-null linked list
#     if head1:
#         tail.bottom = head1
#     else:
#         tail.bottom = head2

#     return dummy.bottom

# def flatten(root):
#     if root is None or root.next is None:
#         return root

#     # Recur for next list
#     root.next = flatten(root.next)

#     # Now merge the current and next list
#     root = merge(root, root.next)

#     # Return the root
#     return root
    
         


# head = Node(5)
# head.bottom = Node(7)
# head.bottom.bottom = Node(8)

# head.next = Node(10)
# head.next.bottom = Node(20)

# head.next.next = Node(19)
# head.next.next.bottom = Node(22)

# head.next.next.next = Node(28)
# head.next.next.next.bottom = Node(40)
# head.next.next.next.bottom.bottom = Node(45)


# def printList(node):
#     while node is not None:
#         print(node.data, end=' ')
#         node = node.bottom
#     print()
    
# root = flatten(head)
# print(printList(root))



# [Approach 3] Using Priority Queues - O(n * m * log(n)) Time and O(n) Space---------------------

from heapq import heappush, heappop


class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.bottom = None


# Utility function to insert a node at beginning
# of the linked list
def push(head, data):

    # 1 & 2: Allocate the Node & Put in the data
    newNode = Node(data)

    # Make next of newNode as head
    newNode.bottom = head

    # Move the head to point to newNode
    head = newNode

    # Return to link it back
    return head


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.bottom is not None:
            print(" -> ", end="")
        node = node.bottom
    print()


# Class to compare two node objects
class Cmp:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data


def flatten(root):
    pq = []
    head = None
    tail = None

    # Pushing main link nodes into priority_queue
    while root:
        heappush(pq, Cmp(root))
        root = root.next

    # Extracting the minimum node while the priority
    # queue is not empty
    while pq:
        minNode = heappop(pq).node

        if head is None:
            head = minNode
            tail = minNode
        else:
            tail.bottom = minNode
            tail = tail.bottom

        # If we have another node at the bottom of the popped
        # node, push that node into the priority queue
        if minNode.bottom:
            heappush(pq, Cmp(minNode.bottom))
            minNode.bottom = None

    return head





