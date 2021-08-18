import unittest

from bst.convert_sorted_array_to_bst import sorted_array_to_bst
from bst.find_good_node import count_good_nodes
from bst.is_same_tree import is_same_tree
from bst.is_symmetric import is_symmetric
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

    def test_sorted_array_to_bst_when_only_one_item(self):
        self.assertEqual(sorted_array_to_bst([0]).value, TreeNode(0).value)

    def test_is_same_tree(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root2 = TreeNode(1)
        root2.right = TreeNode(2)
        self.assertFalse(is_same_tree(root1, root2))

    def test_is_symmetric(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        self.assertFalse(is_symmetric(root1))


if __name__ == '__main__':
    unittest.main()
