class Node:
    def __init__(self, value):
        self.head = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node or None = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return self
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            self.length += 1
        cur_node.next = new_node
        return self
