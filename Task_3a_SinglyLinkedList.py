class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None                

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:            
            self.tail = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_by_value(self, value):
        prev = None
        current = self.head
        while current is not None:
            if current.data == value:
                if prev is None:                 # deleting the head
                    self.head = current.next
                else:                            # deleting a middle or last node
                    prev.next = current.next
                if current is self.tail:         # deleted the last node: move tail back
                    self.tail = prev
                return True
            prev = current
            current = current.next
        return False                             # value not found

    def traverse(self):
        stops = []
        current = self.head
        while current is not None:
            stops.append(current.data)
            current = current.next
        return stops
