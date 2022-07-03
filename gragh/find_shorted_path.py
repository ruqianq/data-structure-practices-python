# Breadth first search

from collections import deque

# directed graph
from gragh.gragh import Graph
from gragh.vertex import Vertex


def check_route_between_vertex(graph: Graph, start_node: int or str, end_node: int or str) -> bool:
    # Utilize queue in BFS
    if graph.get_vertex(start_node) is None or graph.get_vertex(end_node) is None:
        return False
    q = deque()
    q.append(start_node)
    while len(q) > 0:
        node: int or str = q.popleft()
        cur_vertex: Vertex = graph.get_vertex(node)
        cur_vertex.visited = True
        for n in cur_vertex.get_adjacent():
            if not n.visited:
                n.visited = True
                q.append(n.node)
                n.prev = cur_vertex
                if n.node == end_node:
                    return True
    return False


def print_shortest_route(graph: Graph, start_node: int or str, end_node: int or str) -> list:
    if check_route_between_vertex(graph, start_node, end_node) is False:
        return []
    else:
        node = graph.get_vertex(end_node)
        route: list = []
        while node:
            route.append(node.node)
            node = node.prev
        route.reverse()
        return route
