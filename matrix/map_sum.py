class MapSum(object):

    def __init__(self):
        self.d = {}

    def insert(self, key, val):
        self.d[key] = val

    def sum(self, prefix):
        return sum(self.d[i] for i in self.d if i.startswith(prefix))


class Node:
    def __init__(self, node_key, node_value):
        self.node_key = node_key
        self.node_value = node_value
        self.next = None


class MapSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None


    def insert(self, key, val):
        node = Node(key, val)

        if self.head is None:
            self.head = node
            return self
        if self.head.node_key == key:
            self.head.node_value = val
            return self
        curser = self.head
        while curser.next and curser.next.node_key != key:
            curser = curser.next
        curser.next = node
        if self.head.node_key == key:
            self.head.node_value = val
            return self
        return self


    def sum(self, prefix):
        sum_of_val = 0
        q = []
        node = self.head
        q.append(node)
        while len(q) > 0:
            node = q.pop(0)
            if node.node_key.startswith(prefix):
                sum_of_val += node.node_value
            if node.next:
                q.append(node.next)

        return sum_of_val