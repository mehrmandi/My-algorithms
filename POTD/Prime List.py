class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nearest_prime(n):
    if is_prime(n):
        return n

    lower, upper = n - 1, n + 1

    while True:
        if lower > 1 and is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1
        

def replace_with_nearest_prime(head):
    current = head
    while current:
        current.val = nearest_prime(current.val)
        current = current.next
    return head

        
head = Node(2)
head.next = Node(6)
head.next.next = Node(10)
print(replace_with_nearest_prime(head))


        

        
        



