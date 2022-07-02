class Vertex:
    def __init__(self, node):
        self.node = node
        self.adjacent = {}

    def get_adjacent(self):
        return self.adjacent.keys()
