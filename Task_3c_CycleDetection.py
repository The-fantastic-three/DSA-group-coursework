class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        if slow is fast:          # they met -> cycle
            return True
    return False                  # have reached the end -> no cycle


# --- Test 1: Acyclic list ---
a = Node("Main Gate")
b = Node("Hostels")
c = Node("Town Centre")
a.next = b
b.next = c
print("Test 1 (Acyclic):", has_cycle(a))  # False

# --- Test 2: Cyclic list ---
c.next = b
print("Test 2 (Cyclic):", has_cycle(a))   # True
