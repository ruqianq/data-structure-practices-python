import unittest

from bst.convert_sorted_array_to_bst import sorted_array_to_bst
from bst.find_good_node import count_good_nodes
from bst.is_balanced import get_height, is_balanced
from bst.is_same_tree import is_same_tree
from bst.is_symmetric import is_symmetric
from bst.path_sum import has_path_sum
from bst.sum_path_binary import sum_root_to_leaf
from bst.tree_path import binary_tree_paths
from bst.treenode import TreeNode

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(3)
root1.left.left.left = TreeNode(4)
root1.left.left.right = TreeNode(4)


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
        root5 = TreeNode(1)
        root5.left = TreeNode(2)
        root6 = TreeNode(1)
        root6.right = TreeNode(2)
        self.assertFalse(is_same_tree(root5, root6))

    def test_is_symmetric(self):
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        self.assertFalse(is_symmetric(root4))

    def test_get_height(self):
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        self.assertEqual(get_height(root3), 2)

    def test_is_balanced(self):
        root2 = TreeNode(3)
        root2.left = TreeNode(9)
        root2.right = TreeNode(20)
        root2.right.left = TreeNode(15)
        root2.right.right = TreeNode(7)
        self.assertTrue(is_balanced(root2))

    def test_is_balanced_1(self):
        self.assertFalse(is_balanced(root1))

    def test_has_path_sum(self):
        self.assertTrue(has_path_sum(root1, 3))

    def test_binary_tree_paths(self):
        root0 = TreeNode(1)
        root0.left = TreeNode(2)
        root0.left.right = TreeNode(5)
        root0.right = TreeNode(3)
        self.assertEqual(binary_tree_paths(root0), ['1->2->5', '1->3'])

    def test_sum_root_to_leaf(self):
        root0 = TreeNode(1)
        root0.left = TreeNode(0)
        root0.left.left = TreeNode(0)
        root0.left.right = TreeNode(1)
        root0.right = TreeNode(1)
        root0.right.left = TreeNode(0)
        root0.right.right = TreeNode(1)
        self.assertEqual(sum_root_to_leaf(root0), 22)


if __name__ == '__main__':
    unittest.main()
