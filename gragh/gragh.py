from .vertex import Vertex


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0

    def get_vertex(self, node: int or str) -> Vertex or None:
        if node in self.vertex_dict.keys():
            return self.vertex_dict[node]
        else:
            return None

    def add_vertex(self, node: int or str):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertex_dict[node] = new_vertex
        return new_vertex

    def add_edge(self, frm: int or str, to: int or str):
        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            self.add_vertex(to)

        fro_vertex = self.get_vertex(frm)
        to_vertex = self.get_vertex(to)
        fro_vertex.add_adjacent(to_vertex)
        to_vertex.add_adjacent(fro_vertex)
