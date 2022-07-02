import unittest

from gragh.find_shorted_path import check_route_between_vertex
from gragh.gragh import Graph

g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(3, 5)


class TestGraph(unittest.TestCase):

    def test_get_vertex(self):
        output_vertex = g.get_vertex(1)
        self.assertEqual(output_vertex.node, 1)

    def test_add_edge(self):
        edge1 = g.get_vertex(1)
        self.assertEqual([2, 3], [n.node for n in edge1.adjacent])

    def test_check_route_between_vertex(self):
        self.assertTrue(check_route_between_vertex(g, 1, 6))

    def test_check_route_between_vertex_when_node_is_not_included(self):
        self.assertFalse(check_route_between_vertex(g, 9, 6))
