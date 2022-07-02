# Breadth first search

from collections import deque

# directed graph
from gragh.gragh import Graph
from gragh.vertex import Vertex


def check_route_between_vertex(graph: Graph, start_node: Vertex, end_node: Vertex) -> bool:
    # Utilize queue in BFS
    if graph.vertex_dict(start_node) is None or graph.vertex_dict(end_node) is None:
        return False
    q = deque()

    q.append(start_node)
    while len(q) != 0:
        node: Vertex = q.popleft()
        if node is not None:
            for n in node.get_adjacent():
                if n not in q:
                    if n == end_node:
                        return True
                    else:
                        q.append(n)
    return False
