class ListNode:
    """A node in a singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Create the linked list: 1 -> 2 -> 3 -> 4

tail = ListNode(None)
head = ListNode(1)
node2 = ListNode(2)
head.next = node2
print(id(head.next), id(node2), (head.next) is (node2))
print(head.next, node2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = tail
# 2. Find and print the last node
if not head:
    print("The list is empty.")
else:
    # Start at the beginning of the list
    current = head
    
    # Traverse until the *next* node is None
    while current.next:
        current = current.next
        print(f"current val is {current.val}")

    # Now, 'current' is the last node
    