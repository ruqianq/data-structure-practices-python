import unittest

from bst.check_bst import check_bst
from bst.convert_sorted_array_to_bst import sorted_array_to_bst
from bst.diameter_of_tree import diameter_of_binary_tree_2, diameter_of_binary_tree
from bst.find_good_node import count_good_nodes
from bst.is_balanced import is_balanced, check_balanced
from bst.get_height import get_height
from bst.is_same_tree import is_same_tree
from bst.is_symmetric import is_symmetric
from bst.path_sum import has_path_sum
from bst.sum_path_binary import sum_root_to_leaf
from bst.tree_path import binary_tree_paths, convert_binary_tree_to_linked_list_by_depth_dfs
from bst.tree_node import TreeNode
from link_list.linked_list import LinkedList

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
        root2.left.left = TreeNode(32)
        root2.left.left = TreeNode(90)
        self.assertTrue(is_balanced(root2))

    def test_is_balanced_1(self):
        self.assertFalse(is_balanced(root1))

    def test_is_balanced_3(self):
        root2 = TreeNode(3)
        root2.left = TreeNode(9)
        root2.right = TreeNode(20)
        root2.right.left = TreeNode(15)
        root2.right.right = TreeNode(7)
        root2.left.left = TreeNode(32)
        root2.left.left = TreeNode(90)
        self.assertTrue(check_balanced(root2))

    def test_has_path_sum(self):
        self.assertTrue(has_path_sum(root1, 3))

    def test_binary_tree_paths(self):
        root0 = TreeNode(1)
        root0.left = TreeNode(2)
        root0.left.right = TreeNode(5)
        root0.left.right.right = TreeNode(6)
        root0.right = TreeNode(3)
        self.assertEqual(binary_tree_paths(root0), ['1->2->5->6', '1->3'])

    def test_convert_binary_tree_to_linked_list_by_depth_dfs(self):
        root0 = TreeNode(1)
        root0.left = TreeNode(2)
        root0.left.right = TreeNode(5)
        root0.left.right.right = TreeNode(6)
        root0.right = TreeNode(3)

        linked_list0 = LinkedList().append(1)

        linked_list1 = LinkedList().append(1)
        linked_list1.append(2)
        linked_list1.append(3)

        linked_list2 = LinkedList().append(5)

        linked_list3 = LinkedList().append(6)

        expected_arr = [linked_list0, linked_list1, linked_list2, linked_list3]
        test_arr = convert_binary_tree_to_linked_list_by_depth_dfs(root0)
        self.assertEqual(test_arr[0].head.head, expected_arr[0].head.head)
        self.assertEqual(test_arr[2].head.head, expected_arr[2].head.head)

    def test_sum_root_to_leaf(self):
        root0 = TreeNode(1)
        root0.left = TreeNode(0)
        root0.left.left = TreeNode(0)
        root0.left.right = TreeNode(1)
        root0.right = TreeNode(1)
        root0.right.left = TreeNode(0)
        root0.right.right = TreeNode(1)
        self.assertEqual(sum_root_to_leaf(root0), 22)

    def test_diameter_of_binary_tree_2(self):
        self.assertEqual(diameter_of_binary_tree_2(root1), 4)

    def test_diameter_of_binary_tree(self):
        self.assertEqual(diameter_of_binary_tree(root1), 4)

    def test_sorted_array_to_bst(self):
        sorted_array = [1, 3, 5, 7, 8, 9, 100]
        bst = sorted_array_to_bst(sorted_array)
        height = get_height(bst)
        self.assertEqual(bst.value, 7)
        self.assertEqual(height, 3)

    def test_check_bst_when_it_is_a_bst(self):
        root0 = TreeNode(11)
        root0.left = TreeNode(9)
        root0.left.left = TreeNode(8)
        root0.left.right = TreeNode(10)
        root0.right = TreeNode(12)
        root0.right.right = TreeNode(15)
        self.assertTrue(check_bst(root0))

    def test_check_bst_when_it_is_not_a_bst(self):
        root0 = TreeNode(11)
        root0.left = TreeNode(9)
        root0.left.left = TreeNode(8)
        root0.left.right = TreeNode(10)
        root0.right = TreeNode(12)
        root0.right.right = TreeNode(10)
        self.assertFalse(check_bst(root0))


if __name__ == '__main__':
    unittest.main()
