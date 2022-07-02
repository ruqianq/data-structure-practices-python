from gragh.vertex import Vertex


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0

    def get_vertex(self, vertex) -> Vertex or None:
        if vertex in self.vertex_dict:
            return self.vertex_dict[vertex]
        else:
            return None
