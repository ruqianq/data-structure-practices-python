class Vertex:
    def __init__(self, node):
        self.node = node
        self.adjacent = []

    def get_adjacent(self):
        return self.adjacent

    def add_adjacent(self, node):
        if node not in self.adjacent:
            return self.adjacent.append(node)
