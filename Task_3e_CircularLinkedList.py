class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert_at_end(self, data):
        node = Node(data)
        if self.tail is None:
            node.next = node              
        else:
            node.next = self.tail.next    # new node -> head
            self.tail.next = node         # old tail -> new node
        self.tail = node

    def traverse_from(self, start):
        node = self._find(start)          # locate the starting stop
        stops, cur = [node.data], node.next
        while cur is not node:            # stop when back at the start
            stops.append(cur.data)
            cur = cur.next
        return stops
    