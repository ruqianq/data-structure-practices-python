class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, node):
        next_node = LinkedList(node)
        if self.value is None:
            self.next = next_node
        return self
