import unittest

from bst.find_good_node import count_good_nodes
from bst.node import Node


class TestBST(unittest.TestCase):

    def test_count_good_nodes_when_only_root(self):
        root = Node(0)
        self.assertEqual(count_good_nodes(root), 1)

    def test_count_good_nodes(self):
        root = Node(3)
        root.left = Node(1)
        root.left.left = Node(3)
        root.right = Node(4)
        root.right.left = Node(1)
        root.right.right = Node(5)
        self.assertEqual(count_good_nodes(root), 4)

    def test_count_good_nodes_2(self):
        root = Node(3)
        root.left = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(2)
        self.assertEqual(count_good_nodes(root), 3)


if __name__ == '__main__':
    unittest.main()
