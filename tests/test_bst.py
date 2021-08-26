import unittest

from bst.convert_sorted_array_to_bst import sorted_array_to_bst
from bst.find_good_node import count_good_nodes
from bst.is_balanced import get_height, is_balanced
from bst.is_same_tree import is_same_tree
from bst.is_symmetric import is_symmetric
from bst.path_sum import has_path_sum
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

    def test_get_height(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        self.assertEqual(get_height(root1), 2)

    def test_is_balanced(self):
        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertTrue(is_balanced(root1))

    def test_is_balanced_1(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(3)
        root1.left.right = TreeNode(3)
        root1.left.left.left = TreeNode(4)
        root1.left.left.right = TreeNode(4)
        self.assertFalse(is_balanced(root1))

    def test_has_path_sum(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(3)
        root1.left.right = TreeNode(3)
        root1.left.left.left = TreeNode(4)
        root1.left.left.right = TreeNode(4)
        self.assertTrue(has_path_sum(root1, 3))


if __name__ == '__main__':
    unittest.main()
