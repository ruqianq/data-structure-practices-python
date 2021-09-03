import unittest

from binary_search.arrange_coins import calculate_sum, arrange_coins
from binary_search.basic import get_mid_lower, get_mid_upper, binary_search
from binary_search.search_insert import search_insert
from binary_search.two_sum_2 import two_sum


class TestBinarySearch(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 7), 4)

    def test_search_insert_2(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 3), 1)

    def test_get_mid_upper(self):
        self.assertEqual(get_mid_upper(0, 3), 2)

    def test_get_mid_lower(self):
        self.assertEqual(get_mid_lower(0, 3), 1)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 5, 6], 6), 3)

    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4), 10)

    def test_arrange_coins(self):
        self.assertEqual(arrange_coins(8), 3)

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [1, 2])

    def test_two_sum_2(self):
        self.assertEqual(two_sum([0, 0, 3, 4], 0), [1, 2])


if __name__ == '__main__':
    unittest.main()
