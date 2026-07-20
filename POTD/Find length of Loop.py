# # [Naive Approach] Using Set – O(n) Time and O(n) Space

# # Python program to count number of nodes
# # in loop in a linked list if loop is present

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None

# # This function detects and counts loop
# # nodes in the list. If loop is not there
# # then returns 0


# def countNodesinLoop(head):

#     visited = set()
#     current = head
#     count = 0

#     while current is not None:

#         # If the node is already visited,
#         # it means there is a loop
#         if current in visited:
#             startOfLoop = current
#             while True:
#                 count += 1
#                 current = current.next
#                 if current == startOfLoop:
#                     break
#             return count

#         # Mark the current node as visited
#         visited.add(current)

#         # Move to the next node
#         current = current.next

#     # Return 0 to indicate that
#     #   there is no loop
#     return 0


# if __name__ == "__main__":

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)

#     head.next.next.next.next.next = head.next

#     print(countNodesinLoop(head))
    
            
# # [Expected Approach] Using Floyd’s Cycle Detection Algorithm – O(n) Time and O(1) Space

# # Python program to count number of nodes
# # in loop in a linked list if loop is present

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None

# Returns count of nodes present in loop.


# def countNodes(node):
#     res = 1
#     curr = node
#     while curr.next != node:
#         res += 1
#         curr = curr.next
#     return res

# # This function detects and counts loop
# #  nodes in the list. If loop is not there
# #  then returns 0


# def countNodesinLoop(head):
#     slow = head
#     fast = head

#     while slow is not None and fast is not None \
#             and fast.next is not None:

#         slow = slow.next
#         fast = fast.next.next

#         # If slow and fast meet at
#         # some point then there is a loop
#         if slow == fast:
#             return countNodes(slow)

#     # Return 0 to indicate that
#     #   there is no loop
#     return 0


# if __name__ == "__main__":

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)

#     # loop from 5 to 2
#     head.next.next.next.next.next = head.next
#     print(countNodesinLoop(head))
    
    
    #  Node structure
    
    
# [Expected Approach] Using Floyd’s Cycle Detection Algorithm - O(n) Time and O(1) Space---------------------------------------------
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Returns count of nodes present in loop.


def countNodes(node):
    res = 1
    curr = node
    while curr.next != node:
        res += 1
        curr = curr.next
    return res

# Detects and Counts nodes in loop


def lengthOfLoop(head):
    slow = head
    fast = head

    while slow is not None and fast is not None \
            and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        # if slow and fast meet at
        # some point then there is a loop
        if slow == fast:
            return countNodes(slow)

    return 0


if __name__ == "__main__":

    head = Node(25)
    head.next = Node(14)
    head.next.next = Node(19)
    head.next.next.next = Node(33)
    head.next.next.next.next = Node(10)

    head.next.next.next.next.next = head.next.next

    print(lengthOfLoop(head))
