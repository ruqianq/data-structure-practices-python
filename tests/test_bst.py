import unittest

from bst.find_good_node import count_good_nodes
from bst.treenode import TreeNode


class TestBST(unittest.TestCase):

    def test_count_good_nodes_when_only_root(self):
        root = TreeNode(0)
        self.assertEqual(count_good_nodes(root), 1)

    def test_count_good_nodes(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        self.assertEqual(count_good_nodes(root), 4)

    def test_count_good_nodes_2(self):
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(count_good_nodes(root), 3)


if __name__ == '__main__':
    unittest.main()
